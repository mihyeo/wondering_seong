from django.shortcuts import render, get_object_or_404
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

def show(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request,'posts/show.html', {'post':post})



def create(request):
    if request.method == "POST":
        image = request.POST.get('image')
        title = request.POST.get('title')
        content = request.POST.get('content')
        product = Product(image=image,title=title,content=content)
        product.save()
        return render(request,'posts/basic.html')

    
    
