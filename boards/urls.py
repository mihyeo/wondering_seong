from django.urls import path
from .views import board_list, board_show, question_show, create_question, question_like_toggle

urlpatterns = [
    path('', board_list, name="board_list"),
    path('<int:id>/', board_show, name="board_show"),
    path('qustions/<int:id>/', question_show, name="question_show"),
    path('create_question/', create_question, name="create_question"),
    path('question_like_toggle/<int:question_id>/', question_like_toggle, name="question_like_toggle"),
]
