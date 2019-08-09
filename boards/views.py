import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Question, Answer, QuestionLike
import pdb
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse


def board_list(request):
    is_question = request.GET.get('is_question')
    context = {
        'boards': Board.objects.all(),
        'questions': Question.objects.all(),
        'is_question': is_question
    }
    return render(request, 'boards/board_list.html', context)


def board_show(request, id):
    board = get_object_or_404(Board, pk=id)
    default_view_count = board.view_count
    board.view_count = default_view_count + 1
    board.save()
   
    return render(request, 'boards/board_show.html', {'board':board})

    
def question_show(request, id):
    question = get_object_or_404(Question, pk=id)
    default_view_count = question.view_count
    question.view_count = default_view_count + 1
    question.save()
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

    return redirect('/boards?is_question=true')


@require_POST
@login_required
def question_like_toggle(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question_like, question_like_created = QuestionLike.objects.get_or_create(question=question, user=request.user)

    if not question_like_created:
        question_like.delete()
        result = "like_cancel"
    else:
        result = "like"

    context = {'likes_count': question.likes_count,
               'result': result}

    return HttpResponse(json.dumps(context), content_type="application/json")
