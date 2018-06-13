from django.db import models
from django.contrib.postgres.fields import JSONField

class Place(models.Model):
    auto_id = models.AutoField(primary_key=True)
    place_id = models.CharField(max_length=200)
    name = models.TextField()
    visited = models.BooleanField()
    types = JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
        return '%s %s' % (self.title, self.body)