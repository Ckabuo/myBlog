from django import forms
from .models import Post, Subscribe, Category, Contact

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
