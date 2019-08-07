from django.urls import path
from .views import before_sex, sex_ing, after_sex, news, show, like_toggle, create_comment, delete_comment

urlpatterns = [
    path('before_sex/', before_sex, name="before_sex"),
    path('sex_ing/', sex_ing, name="sex_ing"),
    path('after_sex/', after_sex, name="after_sex"),
    path('news/', news, name="news"),
    path('show/<int:id>/', show, name="show"),
    path('like_toggle/<int:post_id>/', like_toggle, name="like_toggle"),
    path('<int:post_id>/create_comment/', create_comment, name="create_comment"),
    path('<int:post_id>/delete_comment/<int:comment_id>/', delete_comment, name="delete_comment"),
]
