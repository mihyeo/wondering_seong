from django.urls import path
from .views import sex, news

urlpatterns = [
    path('sex/', sex, name="sex"),
    path('news/', news, name="news"),
    path('b_content/', b_content, name="b_content"),
    path('s_content/', s_content, name="s_content"),
    path('n_content/',n_content, name="n_content"),
]
