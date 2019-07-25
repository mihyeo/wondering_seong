from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile, Post
from django.contrib.auth.decorators import login_required

def post_like_toggle(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    profile = Profile.objects.get(user=user)

    check_like_post = profile.like_posts.filter(id=post_id)

    if check_like_post.exists():
        profile.like_posts.remove(post)
        post.like_count -= 1
        post.save()
    else:
        profile.like_posts.add(post)
        post.like_count += 1
        post.save()

    return redirect('like:post_detail', post_id)

# Create your views here.
