from rest_framework import viewsets

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostList(viewsets.ModelViewSet):

    queryset = Post.objects.all().order_by("-creation_date")
    serializer_class = PostSerializer


class CommentList(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
