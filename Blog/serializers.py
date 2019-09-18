from .models import Blog
from rest_framework import serializers


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('post')


class BlogEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('post')


class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('Blog')

    def create(self, validated_data):
        owner = self.context.get('owner')
        post = Blog.objects.create(owner=owner, **validated_data)
        post.save()
        return post
