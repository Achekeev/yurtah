from .models import Posts
from .serializers import PostSerializer, PostCreateSerializer, PostEditSerializer
from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsPostOwner


class PostView(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostCreateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        context = super(PostCreateView, self).get_serializer_context()
        context.update({
            "owner": self.request.user
        })
        return context


class PostEditView(generics.UpdateAPIView):
    lookup_field = 'pk'
    queryset = Posts.objects.all()
    serializer_class = PostEditSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsPostOwner)
