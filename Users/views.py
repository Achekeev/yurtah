from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import User
from .permissions import IsUserOwner
from .seralizers import UserSerializer, UserCreateSerializer, UserEditSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'


class UserCreate(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        context = super(UserCreate, self).get_serializer_context()
        context.update({
            "owner": self.request.user
        })
        return context


class UserEditView(generics.UpdateAPIView):
    lookup_field = 'pk'
    queryset = User.objects.all()
    serializer_class = UserEditSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsUserOwner)
