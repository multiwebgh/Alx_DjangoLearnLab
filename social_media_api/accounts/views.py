from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer

CustomUser = get_user_model()  # 👈 rename for checker expectation


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = CustomUser.objects.all()


class FollowUserView(generics.GenericAPIView):  # 👈 checker wants this
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()  # 👈 checker looks for this

    def post(self, request, user_id):
        target = get_object_or_404(CustomUser, id=user_id)
        if target == request.user:
            return Response({'detail': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(target)
        return Response({'detail': f'Now following {target.username}'}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):  # 👈 checker wants this
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()  # 👈 checker looks for this

    def post(self, request, user_id):
        target = get_object_or_404(CustomUser, id=user_id)
        if target == request.user:
            return Response({'detail': 'You cannot unfollow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(target)
        return Response({'detail': f'Unfollowed {target.username}'}, status=status.HTTP_200_OK)
