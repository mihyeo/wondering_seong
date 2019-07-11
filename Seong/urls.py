from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts.views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("allauth.urls")),
    path('', main, name="main"),
    path('posts/', include('posts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

