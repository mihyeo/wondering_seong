from django.urls import path
from .views import sex, news

urlpatterns = [
    path('sex/', sex, name="sex"),
    path('news/', news, name="news"),
]
