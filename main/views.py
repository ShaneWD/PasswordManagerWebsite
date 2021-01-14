from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Location
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from django.contrib.auth.hashers import check_password
from .encryption import *

# Create your views here.
@login_required
def home(request):
    user = request.user
    location = Location.objects.filter(author = user)
    context = {
        'location': location
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
        'master_password',
    ]

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user

        form_master_password = form.instance.master_password

        user_password = self.request.user.password

        if not check_password(form_master_password, user_password):
            return HttpResponse("<h1>Error</h1>")
        
        website_password = form.instance.website_password

        form.instance.website_password = encrypt(form_master_password.encode(), website_password.encode())
        form.instance.website_password = encrypt(form_master_password.encode(), form.instance.website_password.encode())
        # to encrypt twice

        form_master_password = 'DEFAULT'
        return super().form_valid(form)

@login_required
def check(request):
    password = 'admin'
    currentpassword= request.user.password #hashed password in database
    if check_password(password, currentpassword):
        return HttpResponse("<h1>True</h1>")
    else:
        return HttpResponse("<h1>False</h1>")
        # http://www.learningaboutelectronics.com/Articles/How-to-check-a-password-in-Django.php 

@login_required
def view(request, pk):

    location = Location.objects.get(id=pk)

    return HttpResponse(location)

