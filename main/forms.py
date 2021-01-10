from django import forms 

from .models import Location

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            'author',
            'website_name',
            'website_link',
            'website_username',
            'website_password',
            'website_notes',
        ]