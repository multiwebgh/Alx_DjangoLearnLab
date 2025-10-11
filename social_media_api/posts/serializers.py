from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment,Like
User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        source='author', queryset=User.objects.all(), write_only=True, required=False
    )

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_id', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

    def create(self, validated_data):
        # If author provided through context (recommended), use that
        if 'author' not in validated_data and 'request' in self.context:
            user = self.context['request'].user
            validated_data['author'] = user
        return super().create(validated_data)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        source='author', queryset=User.objects.all(), write_only=True, required=False
    )

    class Meta:
        model = Post
        fields = ['id', 'author', 'author_id', 'title', 'content', 'created_at', 'updated_at', 'comments']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at', 'comments']

    def create(self, validated_data):
        # Set author from request if not provided explicitly
        if 'author' not in validated_data and 'request' in self.context:
            validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

User = get_user_model()

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all(), write_only=True, required=False)

    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'user_id', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']