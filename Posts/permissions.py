from rest_framework.permissions import BasePermission
from .models import Posts


class IsPostOwner(BasePermission):
    def has_permission(self, request, view):
        if 'pk' not in view.kwargs:
            return False
        post = Posts.objects.get(pk=view.kwargs['pk'])
        if post.owner == request.user:
            return True
