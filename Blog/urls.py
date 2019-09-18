from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogView, PostEditView, PostCreateView

router = DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('newpost/', PostCreateView, name='post_create'),
    path('editpost/<int:pk>/', PostEditView, name='post_edit'),
    path('postlist/api/', PostView.as_view({'get': 'list'}), name='post_list'),
]
