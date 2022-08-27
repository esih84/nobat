from django.urls import path
from .views import *
app_name = "nobat"
urlpatterns = [
    path('login/', LoginAPI.as_view(), name="login")
]