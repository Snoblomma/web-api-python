from django.db import models
from django.contrib.postgres.fields import ArrayField

class Category(models.Model):
    auto_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Place(models.Model):
    auto_id = models.AutoField(primary_key=True)
    place_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    visited = models.BooleanField()
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
