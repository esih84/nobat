from django.urls import path
from .views import *
app_name = "nobat"
urlpatterns = [
    path('register/', RegistrationView.as_view(), name="register"),
    path('login/', LoginAPI.as_view(), name="login")
]