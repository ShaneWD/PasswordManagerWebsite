from django import forms
from .models import Location

class LocationUpdateForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            'website_name',
            'website_link',
            'website_username',
            # 'website_password',
            'website_notes',
        ]