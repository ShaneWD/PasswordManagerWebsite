from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import check_password
# Create your views here.


@login_required
def account(request):
    if request.method =="POST":
        master_password = request.user.password
        post_password = request.POST.get("password_field")
        if not check_password(post_password, master_password):
            messages.error(request, "Password doesn't match!")
            context = {
                'user': request.user,
                'confirmed': False, 
            }
            return render(request, "users/account.html", context)

        else:
            post_password = request.POST.get("new_password")
            user = User.objects.get(username=request.user)
            user.set_password(post_password)
            user.save()
            context = {
                'confirmed': True,
            }
            return render(request, "users/account.html", context)
    
    context = {
        'user': request.user,
        'confirmed': False,
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

