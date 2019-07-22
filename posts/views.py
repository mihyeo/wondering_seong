from django.shortcuts import render
from .models import Post
import pdb


def basic(request):
    posts = Post.objects.filter(category=0)
    context = {
        'posts': posts
    }
    return render(request, 'posts/basic.html', context)


def sex(request):
    posts = Post.objects.filter(category=1)
    
    context = {
        'posts': posts
    }
    return render(request, 'posts/sex.html', context)


def news(request):
    posts = Post.objects.filter(category=2)
    context = {
        'posts': posts
    }
    return render(request, 'posts/news.html', context)