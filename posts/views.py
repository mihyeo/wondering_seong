import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comment
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import pdb


def basic(request):
    query = request.GET.get('query')
    if query:
        posts = Post.objects.filter(title__contains=query)
    else:
        query = ""
        posts = Post.objects.filter(category=0)

    context = {
        'posts': posts,
        'query': query
    }
    return render(request, 'posts/basic.html', context)


def before_sex(request):
    posts = Post.objects.filter(category=1)
    
    context = {
        'posts': posts
    }
    return render(request, 'posts/before_sex.html', context)


def sex_ing(request):
    posts = Post.objects.filter(category=2)
    
    context = {
        'posts': posts
    }
    return render(request, 'posts/sex_ing.html', context)


def after_sex(request):
    posts = Post.objects.filter(category=3)
    
    context = {
        'posts': posts
    }
    return render(request, 'posts/after_sex.html', context)


def news(request):
    posts = Post.objects.filter(category=4)
    context = {
        'posts': posts
    }
    return render(request, 'posts/news.html', context)

def show(request, id):
    post = get_object_or_404(Post, pk=id)
    post.view_count = post.view_count + 1
    post.save()
    context = {
        'post': post,
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


@require_POST
@login_required
def like_toggle(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_like, post_like_created = post.like_set.get_or_create(user=request.user)

    if not post_like_created:
        post_like.delete()
        result = "like_cancel"
    else:
        result = "like"

    context = {'likes_count': post.likes_count,
               'result': result}

    return HttpResponse(json.dumps(context), content_type="application/json")


@require_POST
@login_required
def create_comment(request, post_id):
    if request.method == "POST":
        user = request.user
        if user.is_anonymous:
            return redirect('account_login')
        post = get_object_or_404(Post, pk=post_id)
        body = request.POST.get('body')
        comment = Comment.objects.create(user=user, post=post, body=body)
        context = {
            'username': user.username,
            'body': comment.body,
            'is_same': user == comment.user,
            'comment_pk': comment.pk
        }
        return HttpResponse(json.dumps(context), content_type="application/json")


def delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('show', post_id)
    
    
