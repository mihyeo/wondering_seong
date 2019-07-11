from django.contrib import admin
from .models import Board, Question


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
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


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
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
        'user',
        'created_at',
        'updated_at',
    )