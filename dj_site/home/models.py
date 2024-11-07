from django.db import models

class Category3(models.Model):
    name = models.CharField(max_length=255)