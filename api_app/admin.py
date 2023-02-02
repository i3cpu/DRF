from django.contrib import admin

from api_app.models import Post, Category

admin.site.register(Post)
admin.site.register(Category)