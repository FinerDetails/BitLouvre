from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("gallery:index")
    else:
        form = NewUserForm()
    return render(request, "users/register.html", {"register_form":form})
    
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("gallery:index")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"login_form":form})

def logout_request(request):
    logout(request)
    return redirect("users:logout")