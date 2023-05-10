from django import forms
from .models import Post, Subscribe

class PostForm(forms.ModelForm):
    # categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    # images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False,)
    class Meta:
        model = Post
        fields = ['title','body','cover_image']


class SubForm(forms.ModelForm):
    # categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    # images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False,)
    class Meta:
        model = Subscribe
        fields = ['email']