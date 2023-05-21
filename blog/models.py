from django.db import models
from datetime import datetime
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, default= User)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    date_posted = models.DateTimeField(default=datetime.now)
    categories = models.ManyToManyField(Category)
    cover_image = models.ImageField(upload_to='cover_images/',blank= True)

    def __str__(self):
        return self.title

class Subscribe(models.Model):
    email = models.EmailField()#CharField(max_length=200)

class BlogPost(models.Model):
    # ...
    anon_likes = models.TextField(blank=True, null=True)

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    comment = models.TextField()
    
