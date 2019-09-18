from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'contacts', 'info', 'owner', 'id')


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','contacts', 'info')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'contacts', 'info')

    def create(self, validated_data):
        owner = self.context.get('owner')
        blog = User.objects.create(owner=owner, **validated_data)
        blog.save()
        return blog
