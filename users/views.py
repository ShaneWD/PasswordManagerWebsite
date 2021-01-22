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
            messages.error(request, "Incorrect Master Password")
            context = {
                'user': request.user,
                'confirmed': False, 
            }
            return render(request, "users/account.html", context)

        else:
            post_password = request.POST.get("new_password1")
            if post_password != request.POST.get("new_password2"):
                messages.error(request, f""" New passwords do not match!""")
                context = {
                'user': request.user,
                'confirmed': False, 
                }
                return render(request, "users/account.html", context)
            user = User.objects.get(username=request.user)
            user.set_password(post_password)
            user.save()
            messages.success(request, f""" Password for "{user}" was changed!""")
            change_master_secondary(request, post_password, user)
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
            messages.success(request, f""" "{user}" Has Been Deleted""")

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

def change_master_secondary(request, password, user):
    #for location in Location.objects.filter(author=user):
        #print(location.objects.all)
    #user = User.objects.filter(username=user).first()
    print(Location.objects.filter(author=user).all())

    for i, c in enumerate(Location.objects.filter(author=user)):
        print i, c, type(c)     
