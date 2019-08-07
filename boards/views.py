from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Question, Answer
import pdb
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def board_list(request):
    context = {
        'boards': Board.objects.all()
    }
    return render(request, 'boards/board_list.html', context)


def board_show(request, id):
    board = get_object_or_404(Board, pk=id)
    context = {
        'board': board
    }
    return render(request, 'boards/board_show.html', context)


def question_list(request):
    context = {
        'questions': Question.objects.all()
    }
    return render(request, 'boards/question_list.html', context)

    
def question_show(request, id):
    question = get_object_or_404(Question, pk=id)
    try:
        answer = question.answer
    except:
        answer = None
    context = {
        'question': question,
        'answer': answer,
    }
    return render(request, 'boards/question_show.html', context)


@login_required
@require_POST
def create_question(request):
    user = request.user
    title = request.POST.get('title')
    content = request.POST.get('content')
    Question.objects.create(
        user=user,
        title=title,
        content=content
    )
    return redirect('question_list')
