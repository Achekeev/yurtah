from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostCreateView, PostEditView, PostView

router = DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('newpost/', PostCreateView, name='post_create'),
    path('editpost/<int:pk>/', PostEditView, name='post_edit'),
    path('post/list/', PostView.as_view({'get': 'list'}), name='post_list'),
]
