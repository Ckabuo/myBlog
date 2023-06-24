from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import PostForm, SubForm, CreateCategoryForm, ContactForm
from .forms import SignupForm
from .models import Post, BlogPost, Category
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
import os
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def home(request, c_filter= ""):
    posts = Post.objects.all()
    categories = Category.objects.all()
    is_admin = request.user.is_staff or request.user.is_superuser
    if len(c_filter) !=0:
        posts = posts.filter(categories__slug=c_filter)
    if request.method == 'POST':
        c_form = ContactForm(request.POST)
        # print(c_form )
        form = SubForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        if c_form.is_valid():
            c_form.save()
            # post = c_form.save(commit=False)
            # post.save()
            # c_form.save_m2m()
            
        return redirect('home')
    else:
        form = SubForm()
        cont_form = ContactForm()
    return render(request, 'index.html', {"posts": posts, "Subform": form,'categories': categories, 'cont_form': cont_form, 'is_admin':is_admin})

def get_anon_user_id(request):
    return request.META.get('REMOTE_ADDR')

def BlogPostLike(request, pk):
    post = get_object_or_404(BlogPost, id=request.POST.get('blogpost_id'))
    anon_user_id = get_anon_user_id(request)
    anon_likes_list = post.anon_likes.split(',') if post.anon_likes else []

    if anon_user_id in anon_likes_list:
        anon_likes_list.remove(anon_user_id)
    else:
        anon_likes_list.append(anon_user_id)

    post.anon_likes = ','.join(anon_likes_list)
    post.save()
    return HttpResponseRedirect(reverse('blogpost-detail', args=[str(pk)]))

class BlogPostDetailView(DetailView):
    # ...
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        anon_likes_connected = get_object_or_404(BlogPost, id=self.kwargs['pk'])
        anon_user_id = get_anon_user_id(self.request)
        anon_likes_list = anon_likes_connected.anon_likes.split(',') if anon_likes_connected.anon_likes else []
        anon_liked = anon_user_id in anon_likes_list
        data['number_of_anon_likes'] = len(anon_likes_list)
        data['post_is_anon_liked'] = anon_liked
        return data

def vincheck(request):
    return render(request, 'vincheck.html')

@login_required
@user_passes_test(lambda u: u.is_staff)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.save()
            form.save_m2m()
            
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # for image in post.image_set.all():
    #     # delete the physical image file from the file system
    #     if os.path.isfile(image.image.path):
    #         os.remove(image.image.path)
    #     # delete the Image object from the database
    #     image.delete()
    post.delete()
    return redirect('home')

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    post.body = post.body.split("\n")
    # print(post.categories())
    return render(request, 'blog_template.html', {'post': post})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def manage_slugs(request):
    categories_exist = Category.objects.all().exists()
    categories = Category.objects.all()
    return render(request, 'manage_slugs.html', {'categories': categories, 'cat_exist': categories_exist})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    category.delete()
    return redirect('category_list')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def create_category(request):
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            slug = form.cleaned_data['slug']
            i = 0
            while Category.objects.filter(slug=slug).exists():
                i += 1
                slug = f'{slug}-{i}'
            category = Category.objects.create(name=name, slug=slug)
            form = CreateCategoryForm()
            return redirect('create_category')
    else:
        form = CreateCategoryForm()
    # print(form.as_p())
    # print(9)
    categories = Category.objects.all()
    return render(request, 'create_category.html', {'form': form, 'categories': categories})


def logout_view(request):
    logout(request)
    return redirect('home')

class CustomLoginView(LoginView):
    template_name = 'index.html'#'login.html'
    success_url = reverse_lazy('home')


# from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect(reverse('manage_users'))


@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('manage_users')
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'edit_user.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def manage_accounts(request):
    users = User.objects.all()
    return render(request, 'manage_accounts.html', {'users': users})
