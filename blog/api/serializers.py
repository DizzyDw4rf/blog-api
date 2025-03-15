from rest_framework import serializers

from .models import Post


class PostSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'category',
            'tags',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at',]
