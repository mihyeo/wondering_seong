from django.shortcuts import render, get_object_or_404
from .models import Board, Question, Answer
import pdb

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
    answer = question.answer
    context = {
        'question': question,
        'answer': answer,
    }
    return render(request, 'boards/question_show.html', context)