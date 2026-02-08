from django.urls import path
from .api import RegisterAPI, LoginAPI, LogoutAPI
from .views import login_view,register_view,logout_view

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('logout/', LogoutAPI.as_view()),

    path("login-ui/", login_view, name="login-ui"),
    path("register-ui/", register_view, name="register-ui"),
    path("logout-ui/", logout_view, name="logout-ui"),


]
