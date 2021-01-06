from django.shortcuts import render
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    form = UserRegisterForm()
    context = {
        "form": form,
    }
    return render(request, "users/register.html", context)