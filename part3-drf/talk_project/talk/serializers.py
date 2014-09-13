from django.contrib.auth.models import User
from rest_framework import serializers
from talk.models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class PostSerializerGet(serializers.ModelSerializer):
    author = UserSerializer(source='author')

    class Meta:
        model = Post
        fields = ['id', 'author', 'text', 'created', 'updated']


class PostSerializerPost(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )

    class Meta:
        model = Post
        fields = ['id', 'author', 'text', 'created', 'updated']
