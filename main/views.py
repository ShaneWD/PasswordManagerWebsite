from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LocationForm
from .models import Location
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    if request.method =="POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("home")
    else:
        form = LocationForm()
    context = {
        # "location":Location.objects.all(),
        "form": form
    }
    return render(request, "main/home.html", context)