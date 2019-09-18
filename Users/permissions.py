from rest_framework.permissions import BasePermission
from .models import User


class IsUserOwner(BasePermission):
    def has_permission(self, request, view):
        if 'pk' not in view.kwargs:
            return False
        user = User.objects.get(pk=view.kwargs['pk'])
        if user.owner == request.user:
            return True
