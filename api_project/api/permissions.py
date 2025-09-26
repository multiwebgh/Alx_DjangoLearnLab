from rest_framework.permissions import BasePermission

class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Anyone can read
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        # Only admins can edit/delete
        return request.user.is_staff