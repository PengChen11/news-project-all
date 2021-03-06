from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=250)
    source = models.URLField()

    def __str__(self):
        return self.title
