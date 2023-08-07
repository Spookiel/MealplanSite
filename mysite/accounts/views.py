from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.


def login(request):
    if request.method == "POST":
        print("POST ATTEMPTED")
        return redirect("index")
    return render(request, "accounts/login.html")
def register(request):
    print(request, "HERE", request.POST)

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created succesfully.")
        return redirect("index")
    return render(request, "accounts/register.html")