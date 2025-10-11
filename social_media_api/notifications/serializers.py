from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()
    recipient = serializers.StringRelatedField()
    target_repr = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'actor', 'verb', 'target_repr', 'unread', 'timestamp']

    def get_target_repr(self, obj):
        # Provide a simple representation of the target object
        if obj.target is None:
            return None
        try:
            return str(obj.target)
        except Exception:
            return None
