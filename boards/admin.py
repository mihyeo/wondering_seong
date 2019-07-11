from django.contrib import admin
from .models import Board


@admin.register(Board)
class PostAdmin(admin.ModelAdmin):
    list_diaply_links = (
        'title',
    )

    search_fields = (
        'title',
    )
    
    list_filter = (
    )

    list_display = (
        'title',
        'created_at',
        'updated_at',
    )
