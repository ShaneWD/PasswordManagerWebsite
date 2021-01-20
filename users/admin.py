from django.contrib import admin
from .models import User
# Register your models here.

class AdminConfig(admin.ModelAdmin):
    exclude = ('password',)

admin.site.register(User, AdminConfig)

 