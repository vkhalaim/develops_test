from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):

    comments = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="comments-detail"
    )

    class Meta:
        model = Post
        fields = [
            "title",
            "link",
            "creation_date",
            "upvotes",
            "author",
            "comments",
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
