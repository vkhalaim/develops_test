from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r"posts", views.PostList, basename="posts")
router.register(r"comments", views.CommentList, basename="comments")

urlpatterns = router.urls
