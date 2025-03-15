from django.urls import path
from .views import *


urlpatterns = [
    path('posts/', PostList.as_view(), name=PostList.name),
    path('posts/<int:pk>/', PostDetail.as_view(), name=PostDetail.name),
]
