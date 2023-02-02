from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=300)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title}'