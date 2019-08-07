from django.urls import path
from .views import board_list, board_show, question_list, question_show, create_question

urlpatterns = [
    path('', board_list, name="board_list"),
    path('<int:id>/', board_show, name="board_show"),
    path('questions/', question_list, name="question_list"),
    path('qustions/<int:id>/', question_show, name="question_show"),
    path('create_question/', create_question, name="create_question"),
]
