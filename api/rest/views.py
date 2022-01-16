from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer, PostSerializer, CommentSerializer
from .serializers import Category, Post, Comment


# Create your views here.
class CategoryModelView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostModelView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentModelView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CategorySerializer
