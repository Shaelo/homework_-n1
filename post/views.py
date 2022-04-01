from django.shortcuts import render

# Create your views here.
from rest_framework.generics import *

from post.models import Post
from post.serializers import PostSerializers


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostCreateView(CreateAPIView):
    serializer_class = PostSerializers


class PostUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
