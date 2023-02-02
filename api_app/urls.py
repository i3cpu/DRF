from django.urls import path, include
from . import views


from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('category',views.CategoryList, basename='CategoryList')
router.register('post/1', views.PostList, basename='PostList')

urlpatterns = [
    path('',include(router.urls)),
]
