from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255, default="default",blank=True, null=True)
    body = models.TextField(default="default",null=True, blank=True)
    auther = models.CharField(max_length=255, default="default",blank=True, null=True)