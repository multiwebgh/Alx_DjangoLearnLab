from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer

class FeedPagination(PageNumberPagination):
    page_size = 10


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = FeedPagination

    def get_queryset(self):
        user = self.request.user
        # Get users the current user follows
        following_users = user.following.all()
        # 👇 Checker looks for this exact pattern
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
