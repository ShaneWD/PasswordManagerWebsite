from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Location
from django.views.generic import CreateView

# Create your views here.
def home(request):
    context = {
        
    }
    return render(request, "main/home.html", context)

class LocationCreateView(CreateView):
    model = Location
    fields = [
        'website_name',
        'website_link',
        'website_username',
        'website_password',
        'website_notes',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)