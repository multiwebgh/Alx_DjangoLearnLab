# posts/views.py
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializer

User = get_user_model()

class FeedPagination(PageNumberPagination):
    page_size = 10

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = FeedPagination

    def get_queryset(self):
        user = self.request.user
        # Authors the user follows
        following_qs = user.following.all()
        # Posts by authors the user follows, ordered newest first
        return Post.objects.filter(author__in=following_qs).order_by('-created_at')
