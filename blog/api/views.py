from rest_framework import generics
from rest_framework import filters

from .models import Post
from .serializers import PostSerilaizer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerilaizer
    search_fields = ['title', 'content', 'category',]
    name = 'post_list'


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerilaizer
    name = 'post_detail'

