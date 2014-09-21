from django.contrib.auth.models import User
from rest_framework import serializers
from talk.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'created', 'updated')
