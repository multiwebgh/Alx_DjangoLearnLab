from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to allow only owners to edit/delete objects.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have `author` attribute
        return getattr(obj, 'author', None) == request.user
