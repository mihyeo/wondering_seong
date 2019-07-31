from django.urls import path
from .views import sex, news, show, like_toggle, create_comment, delete_comment

urlpatterns = [
    path('sex/', sex, name="sex"),
    path('news/', news, name="news"),
    path('show/<int:id>/', show, name="show"),
    path('like_toggle/<int:post_id>/', like_toggle, name="like_toggle"),
    path('<int:post_id>/create_comment/', create_comment, name="create_comment"),
    path('<int:post_id>/delete_comment/<int:comment_id>/', delete_comment, name="delete_comment"),
]
