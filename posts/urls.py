from django.urls import path
from .views import sex, news, show

urlpatterns = [
    path('sex/', sex, name="sex"),
    path('news/', news, name="news"),
    path('show/<int:id>', show, name="show"),
]
