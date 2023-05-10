from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, default= User)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    date_posted = models.DateTimeField(default=datetime.now)
    # categories = models.ManyToManyField(Category)
    cover_image = models.ImageField(upload_to='cover_images/',blank= True)

    def __str__(self):
        return self.title

class Subscribe(models.Model):
    email = models.EmailField()#CharField(max_length=200)

class BlogPost(models.Model):
    # ...
    anon_likes = models.TextField(blank=True, null=True)
