from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import check_password
from main.models import Location
from main.encryption import *
# Create your views here.


@login_required
def account(request):
    if request.method =="POST":
        master_password = request.user.password
        post_password = request.POST.get("password_field")
        if not check_password(post_password, master_password):
            messages.error(request, "Incorrect Master Password")
            context = {
                'user': request.user,
                'confirmed': False, 
            }
            return render(request, "users/account.html", context)

        else:
            requested_password = request.POST.get("new_password1")
            if requested_password != request.POST.get("new_password2"):
                messages.error(request, f""" New passwords do not match!""")
                context = {
                'user': request.user,
                'confirmed': False, 
                }
                return render(request, "users/account.html", context)

            user = User.objects.get(username=request.user)
            user.set_password(requested_password)
            user.save()

            messages.success(request, f""" Password for "{user}" was changed!""")

            change_master_secondary(post_password, user, requested_password)

            context = {
                'confirmed': True,
            }
            return redirect('login')
    
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
    if request.method == 'POST':
        form_master_password = request.POST.get("master_password")
        user_password = request.user.password
        if check_password(form_master_password, user_password):
            username = request.user
            user = User.objects.get(username = username)
            user.delete()
            messages.success(request, f""" User "{user}" has been deleted!""")

            form = UserRegisterForm()
            context = {
                "form": form,
            }

            return render(request, "users/register.html", context)

        else:
            messages.error(request, "Invalid Password")
            return render(request, "users/delete_account.html")
            
    else:
        return render(request, "users/delete_account.html")


def change_master_secondary( password, user, new_pwd):
    for i, c in enumerate(Location.objects.filter(author=user)):
        decrypted = decrypt(password.encode(), c.website_password)
        decrypted = decrypt(password.encode(), decrypted)

        encrypted = encrypt(new_pwd.encode(), decrypted.encode())
        encrypted = encrypt(new_pwd.encode(), encrypted.encode())
        
        c.website_password = encrypted
        c.save()
