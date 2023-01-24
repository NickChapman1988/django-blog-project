from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'blog/home.html')


posts = [
    {
        'author': 'Loonycon',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 25, 2019'
    },
    {
        'author': 'Test',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 25, 2019'
    }
]


def business(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/business.html', context)
