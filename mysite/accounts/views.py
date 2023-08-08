from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
# Create your views here.


def login(request):
    if request.method == "POST":

        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        auth_login(request, user)
        if user is None:
            context = {"error":"Invalid username or password"}
            return render(request, "accounts/login.html", context)
        
        return redirect("index")
    return render(request, "accounts/login.html")
def register(request):
    #print(request, "HERE", request.POST)
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect("index")
        ### Failed to register user
        print(form.errors.as_text)
        context = {"errors": form.errors.as_text}
        return render(request, "accounts/register.html", context)
    return render(request, "accounts/register.html")