from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(default='nothing', max_length=255)
