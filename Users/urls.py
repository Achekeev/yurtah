from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserView, UserCreate, UserEditView

router = DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('create/', UserCreate, name='user_create'),
    path('edit/<int:pk>/', UserEditView, name='company_edit'),
    path('list/api/', UserView.as_view({'get': 'list'}), name='company_list_api'),
]
