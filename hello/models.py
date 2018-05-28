from django.db import models

class Places(models.Model): 
    name = models.CharField('name',max_length=255, blank=False, unique=True)
    placeId = models.CharField('place id',max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_modified = models.DateTimeField('date modified',auto_now=True)
