from django.contrib import admin
from .models import Post, CardImage, Comment

admin.site.site_header = "궁금했성 어드민"
admin.site.site_title = "궁금했성 어드민"
# admin.site.index_title = "개꿀"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_diaply_links = (
        'title',
        'user',
    )

    search_fields = (
        'title',
    )
    
    list_filter = (
        'kinds',
        'category',
    )

    list_display = (
        'title',
        'kinds',
        'category',
        'user',
        'view_count',
        'created_at',
        'updated_at',
    )


@admin.register(CardImage)
class CardImageAdmin(admin.ModelAdmin):
    list_diaply_links = (
        'post',
    )

    search_fields = (
        'post',
    )

    list_display = (
        'image',
        'post',
        'created_at',
        'updated_at',
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'body',
        'user',
        'post',
        'created_at',
        'updated_at',
    )
