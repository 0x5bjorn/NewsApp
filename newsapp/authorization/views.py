from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserForm

"""
    Check if request is POST or GET:
        - If POST, create UserForm object with the parameters provided in the request
        Check form's validity and save it in the database
        Perform login operation and redirect to homepage.html 
        Raise errors if this UserForm object is not valid
        - If GET, create empty UserForm object and send it to registration.html
"""
def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("news:homepage")
        else:
            for field in form:
                messages.error(request, f"{field.errors}")
            return render(request, "authorization/registration.html", {"form": form})
            
    form = UserForm()
    return render(request, "authorization/registration.html", {"form": form})

"""
    Check if request is POST or GET:
        - If POST, create AuthenticationForm object with the parameters provided in the request
        Check form's validity and get username and password from request
        Check if user exists, perform login operation and redirect to homepage.html 
        Raise errors if this AuthenticationForm object is not valid or user does not exists
        - If GET, create empty AuthenticationForm object and send it to login.html
"""
def login_req(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("news:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    return render(request, "authorization/login.html", {"form": form})

"""
    Perform logout operation and redirect to homepage.html
"""
def logout_req(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("news:homepage")