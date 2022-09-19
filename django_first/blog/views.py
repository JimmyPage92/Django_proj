from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

POSTS = [
    {
        'author': 'Michal Pastuszka',
        'title': "Pierwszy artykul",
        'content': 'To jest moj pierwszy artykul',
        'date': '01 September 2022'
    },
    {
        'author': 'Marlena Pastuszka',
        'title': "Drugi artykul",
        'content': 'To jest moj drugi artykul',
        'date': '01 September 2022'
    }
]


def home(request):
    return render(request,'blog/home.html', {'title': 'Home', 'posts': POSTS})

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})