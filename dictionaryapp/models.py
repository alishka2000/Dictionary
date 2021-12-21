from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

class Language(models.Model):
    name = models.CharField(max_length=255)
    is_default = models.TextField()

class Dictionary(models.Model):
    code = models.CharField(max_length=42)
    name = models.TextField()
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
