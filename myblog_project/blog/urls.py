from django.urls import path
from . import views

urlpatterns = [
    path('something/', views.blog_home, name='blog_post'),
]
