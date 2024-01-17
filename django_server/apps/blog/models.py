from django.db import models
from meta.models import ModelMeta
# Create your models here.
class Article(models.Model, ModelMeta):
    title = models.CharField(max_length=255, default="default",blank=True, null=True)
    body = models.TextField(default="default",null=True, blank=True)
    auther = models.CharField(max_length=255, default="default",blank=True, null=True)