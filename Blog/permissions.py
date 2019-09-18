from rest_framework.permissions import BasePermission
from .models import Blog


class IsBlogOwner(BasePermission):
    def has_permission(self, request, view):
        if 'pk' not in view.kwargs:
            return False
        post = Blog.objects.get(pk=view.kwargs['pk'])
        if Blog.owner == request.user:
            return True
