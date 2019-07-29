from django.shortcuts import render, redirect, get_object_or_404
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
    post.view_count = post.view_count + 1
    post.save()
    return render(request,'posts/show.html', {'post':post})



def create(request):
    if request.method == "POST":
        image = request.POST.get('image')
        title = request.POST.get('title')
        content = request.POST.get('content')
        product = Product(image=image,title=title,content=content)
        product.save()
        return render(request,'posts/basic.html')


def like_toggle(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user
    if user.is_anonymous:
        return redirect('account_login')

    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)

    return redirect('show', post_id)

    
    
