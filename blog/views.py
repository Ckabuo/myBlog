from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse
from .forms import PostForm, SubForm
from .models import Post, BlogPost
import os

# Create your views here.
def home(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        print(10)
        form = SubForm(request.POST)
        print(form)
        # if form.is_valid():
        #     post = form.save(commit=False)
        #     post.save()
            
        return redirect('home')
    else:
        form = SubForm()
    return render(request, 'index.html', {"posts": posts, "form": form})

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


def vincheck(request):
    return render(request, 'vincheck.html')

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.save()
            
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

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
    return render(request, 'blog_template.html', {'post': post})

