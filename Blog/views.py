from rest_framework.generics import get_object_or_404
from .models import Blog
from .serializers import BlogSerializer, BlogCreateSerializer, BlogEditSerializer
from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsBlogOwner


class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'


class BlogCreateView(generics.CreateAPIView):
    serializer_class = BlogCreateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        context = super(BlogCreateView, self).get_serializer_context()
        context.update({
            "owner": self.request.user
        })
        return context


class BlogEditView(generics.UpdateAPIView):
    lookup_field = 'pk'
    queryset = Blog.objects.all()
    serializer_class = BlogEditSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsBlogOwner)
