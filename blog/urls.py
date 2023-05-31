from django.urls import path
from . import views

urlpatterns = [
    path('vincheck/', views.vincheck, name='vincheck'),
    path('Nposts/<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('manage_users/edit/<int:user_id>/', views.edit_user, name='edit_user'),
]