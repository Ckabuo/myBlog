"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from blog import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
# from .views import delete_category
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path("blog/",include(("blog.urls","blog"), namespace= "blog")),
    path('Cposts/', views.create_post, name='create_post'),
    path('blogpost-like/<int:pk>', views.BlogPostLike, name="blogpost_like"),
    path('categories/<slug:slug>/delete/', views.delete_category, name='delete_category'),
    path('categories/', views.manage_slugs, name= "manage_slugs"),
    path('create_category/', views.create_category, name='create_category'),
    path('posts/<str:c_filter>/', views.home, name='filt_post_list'),
    path('login/', views.CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('manage/', views.manage_accounts, name='manage_users'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
