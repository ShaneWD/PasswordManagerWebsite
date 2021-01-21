from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
# Create your views here.


@login_required
def account(request):
    
    context = {
        'user': request.user,
    }

    return render(request, "users/account.html", context)


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

@login_required
def delete_account(request):
    username = request.user
    user = User.objects.get(username = username)
    user.delete()
    messages.success(request, f""" "{user}" Has Been Deleted""")

    form = UserRegisterForm()
    context = {
        "form": form,
    }

    return render(request, "users/register.html", context)

