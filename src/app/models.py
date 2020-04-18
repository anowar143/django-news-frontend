from django.db import models

# Create your models here.


class D(models.Model):
    name = models.CharField(max_length=300)
