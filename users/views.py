from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required


def profile(request, id):
    user = get_object_or_404(User, pk = id)
    context = {
        'user': user
    }

    return render(request, 'users/profile.html', context)


@login_required()
# @permission_required('request.user.pk')
def update(request, id):
    user = get_object_or_404(User, pk = id)
    context = {
        'user': user,
        'form': UserChangeForm(instance = user)
    }
    if request.method == "POST":
        form = UserChangeForm(request.POST, request.FILES or None, instance=user)
        if form.is_valid():
            form.save()
        return redirect('main')

    return render(request, 'users/update.html', context)