from django.urls import path
from .views import CustomLoginView, CustomLogoutView
from .views import RegistroUsuarioView

urlpatterns = [
    path("login", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="custom_logout"),
    path("register/", RegistroUsuarioView.as_view(), name="register"),
]