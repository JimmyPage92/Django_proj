from django.shortcuts import render
from .models import Article

# Create your views here.

def home(request):
    return render(request,'blog/home.html', {'title': 'Home page', 'posts': Article.objects.all()})

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})