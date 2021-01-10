from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
# Create your views here.

def account(request):
    return HttpResponse("Account Page")

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()
    context = {
        "form": form,
    }
    return render(request, "users/register.html", context)