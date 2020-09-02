from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "upvotes",
    ]
    list_display_links = [
        "title",
    ]
    fields = [
        (
            "title",
            "link",
        ),
        (
            "author",
            "upvotes",
        ),
    ]
    readonly_fields = [
        "upvotes",
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "author",
        "content",
        "post",
    ]
    list_display_links = [
        "content",
    ]
