from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    main_user = models.ForeignKey(User, on_delete=models.CASCADE, default="DEFAULT VALUE")
    
    website_name = models.CharField(max_length=50, default='DEFAULT VALUE', unique=True)
    website_link = models.URLField(max_length=200, null=True)
    website_username = models.CharField(max_length=50, default='DEFAULT VALUE')
    website_password = models.CharField(max_length=50, default='DEFAULT VALUE')
    website_notes = models.CharField( max_length=50, null=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)

    def __str__(self):
        return self.website_name