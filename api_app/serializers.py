from rest_framework import serializers
from api_app.models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'text', 'category']

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']