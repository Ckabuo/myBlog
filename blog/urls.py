from django.urls import path
from . import views

urlpatterns = [
    path('vincheck/', views.vincheck, name='vincheck'),
]