from django.db import models

class Place(models.Model):
    auto_id = models.AutoField(primary_key=True)
    place_id = models.CharField(max_length=200)
    name = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    visited = models.BooleanField()

def __str__(self):
        return '%s %s' % (self.title, self.body)