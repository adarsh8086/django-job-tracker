from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.
def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )

        if user:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "accounts/login.html", {"error": "Invalid credentials"})

    return render(request, "accounts/login.html")





def register_view(request):
    if request.method == "POST":
        if User.objects.filter(username=request.POST["username"]).exists():
            return render(request, "accounts/register.html", {"error": "User exists"})

        User.objects.create_user(
            username=request.POST["username"],
            password=request.POST["password"],
        )
        return redirect("/login-ui/")

    return render(request, "accounts/register.html")



def logout_view(request):
    logout(request)
    return redirect("/")
