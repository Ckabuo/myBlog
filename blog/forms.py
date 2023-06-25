from django import forms
from .models import Post, Subscribe, Category, Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    # images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False,)
    class Meta:
        model = Post
        fields = ['title','body','cover_image', 'categories']


class SubForm(forms.ModelForm):
    # categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    # images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False,)
    class Meta:
        model = Subscribe
        fields = ['email']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','comment']


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name','slug')

class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already taken')
        return email