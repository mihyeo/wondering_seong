from django.urls import path
from .views import sex, news, show, like_toggle

urlpatterns = [
    path('sex/', sex, name="sex"),
    path('news/', news, name="news"),
    path('show/<int:id>/', show, name="show"),
    path('like_toggle/<int:post_id>/', like_toggle, name="like_toggle"),
]
