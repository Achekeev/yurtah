from .models import Posts
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('post')


class PostEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('post')


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('post')

    def create(self, validated_data):
        owner = self.context.get('owner')
        post = Posts.objects.create(owner=owner, **validated_data)
        post.save()
        return post
