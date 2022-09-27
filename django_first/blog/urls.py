from django.contrib import admin
from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView
from . import views

urlpatterns = [
    path('', ArticleListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/new/', ArticleCreateView.as_view(), name='article-create'),
]
