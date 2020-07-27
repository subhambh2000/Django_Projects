from django.db import models

# Create your models here.
class todomodel(models.Model):
    task = models.CharField(max_length=20)