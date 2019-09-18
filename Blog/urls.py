from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogView, BlogEditView, BlogCreateView

router = DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('newpost/', BlogCreateView, name='blog_create'),
    path('editpost/<int:pk>/', BlogEditView, name='blog_edit'),
    path('postlist/api/', BlogView.as_view({'get': 'list'}), name='blog_list'),
]
