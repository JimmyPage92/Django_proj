from rest_framework.viewsets import generics
from .serializers import ArticleSerializer
from blog.models import Article

# Create your views here.

class GetAllArticles(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()