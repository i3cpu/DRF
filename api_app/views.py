from django.shortcuts import render

from api_app.models import Post, Category
from api_app.serializers import PostSerializer, CategorySerializer


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets, mixins, generics

class CategoryList(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostList(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):   
    queryset = Post.objects.all()
    serializer_class = PostSerializer