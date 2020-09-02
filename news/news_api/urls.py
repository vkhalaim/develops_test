from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r"posts", views.PostViewSet, basename="posts")
router.register(r"comments", views.CommentViewSet, basename="comments")

urlpatterns = router.urls

urlpatterns.append(
    path("posts/<int:pk>/upvote", views.UpvoteView.as_view(), name="upvoting")
)
