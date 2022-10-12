from django.urls import path
from .views import GetAllArticles, GetArticle, CreateArticle, DestroyArticle, UpdateArticle, PatchArticle
urlpatterns = [
    path('articles/', GetAllArticles.as_view(), name='get_articles'),
    path('article/<int:pk>/', GetArticle.as_view(), name='get_article'),
    path('article/create/', CreateArticle.as_view(), name='create_article'),
    path('article/delete/<int:pk>', DestroyArticle.as_view(), name='delete_article'),
    path('article/update/<int:pk>', UpdateArticle.as_view()),
    path('article/allfunc/<int:pk>', PatchArticle.as_view()),
]