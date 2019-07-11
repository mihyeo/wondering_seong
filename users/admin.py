from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_diaply_links = (
        'username',
    )

    search_fields = (
        'username',
        'email',
    )
    
    list_filter = (
    )

    list_display = (
        'username',
        'email',
        'image',
        'is_superuser',
        'created_at',
        'updated_at',
    )
