from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.db.models import Count
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
    likes_count = post.likes.count()
    context = {
        'post': post,
        'likes_count': likes_count
    }
    return render(request,'posts/show.html', context)



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


def create_comment(request, post_id):
    if request.method == "POST":
        user = request.user
        if user.is_anonymous:
            return redirect('account_login')
        post = get_object_or_404(Post, pk=post_id)
        body = request.POST.get('body')
        Comment.objects.create(user=user, post=post, body=body)
        return redirect('show', post_id)


def delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('show', post_id)
    
    
