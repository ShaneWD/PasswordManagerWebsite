from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    website_name = models.CharField(max_length=50, unique=True)
    website_link = models.URLField(max_length=200, null=True)
    website_username = models.CharField(max_length=50)
    website_password = models.CharField(max_length=50)
    website_notes = models.CharField( max_length=50, null=True)

    created = models.DateTimeField( auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.website_name