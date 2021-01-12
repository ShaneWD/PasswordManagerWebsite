from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Location
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from django.contrib.auth.hashers import check_password

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

@login_required
def check(request):
    password = 'admin'
    currentpassword= request.user.password #hashed password in database
    if check_password(password, currentpassword):
        return HttpResponse("True")
    else:
        return HttpResponse("False")
        # http://www.learningaboutelectronics.com/Articles/How-to-check-a-password-in-Django.php 


