from django.urls import path
from .views import *
app_name = "nobat"
urlpatterns = [
    path('register/', RegistrationView.as_view(), name="register"),
    path('register_hair/', RegistrationView_hair_style.as_view(), name="register_hair"),
    path('login/', LoginAPI.as_view(), name="login")
]