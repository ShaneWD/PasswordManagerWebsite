from django.shortcuts import render, redirect
from .forms import UserRegisterForm

# Create your views here.
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

def profile(request):
    return render(request,'users/profile.html')