from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "link",
            "creation_date",
            "upvotes",
            "author",
        ]
        read_only_fields = [
            "votes",
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "author",
            "content",
            "created",
            "post",
        ]
