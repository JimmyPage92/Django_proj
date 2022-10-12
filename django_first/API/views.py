from rest_framework.viewsets import generics
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser
from .serializers import ArticleSerializer
from blog.models import Article


# Create your views here.


class GetAllArticles(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

class GetArticle(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset = Article

class CreateArticle(generics.CreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

class DestroyArticle(generics.DestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article
    permission_classes = [IsAdminUser]

class UpdateArticle(generics.UpdateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

class PatchArticle(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [IsAdminUser]

