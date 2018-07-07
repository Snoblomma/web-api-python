from django.db import models
from django.contrib.postgres.fields import ArrayField

class Place(models.Model):
    auto_id = models.AutoField(primary_key=True)
    place_id = models.CharField(max_length=200)
    name = models.TextField()
    visited = models.BooleanField()
    types = ArrayField(models.CharField(max_length=200))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    auto_id = models.AutoField(primary_key=True)
    category_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

def __str__(self):
        return '%s %s' % (self.title, self.body)