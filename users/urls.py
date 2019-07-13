from django.urls import path
from .views import profile, update

app_name = "users"
urlpatterns = [
    path('<int:id>/', profile, name="profile"),
    path('<int:id>/update/', update, name="update"),
]
