from rest_framework import viewsets, views, generics
from rest_framework.response import Response

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all().order_by("-creation_date")
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UpvoteView(views.APIView):
    def get(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        post.vote()
        return Response({"msg": f"Post: {post.title} was upvoted!"})
