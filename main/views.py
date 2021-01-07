from django.shortcuts import render
from django.http import HttpResponse
from .forms import LocationForm
from .models import Location
# Create your views here.
def home(request):
    form = LocationForm()
    context = {
        "location":Location.objects.all(),
        "form": form
    }
    return render(request, "main/home.html", context)