from django.shortcuts import render
from .models import Article
from django.views.generic.list import ListView # tu bedziemy przechowywac wszystkie artykuly z bloga
from django.views.generic.detail import DetailView
from django.views.generic import CreateView

# Create your views here.

def home(request):
    return render(request,'blog/home.html', {'title': 'Home page', 'posts': Article.objects.all()})

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-data_posted']


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article.html'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'blog/article_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)