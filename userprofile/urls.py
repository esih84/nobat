from django.urls import path
from .views import *
app_name = "userprofile"
urlpatterns = [
    path('update_profile/', create_profile.as_view(), name="update_profile"),
    path('update_profile_user/', create_profile_user.as_view(), name="update_profile_user"),
    path('create_services/', create_service.as_view(), name="create_services"),
    path('upload_photo/', upload_photo.as_view(), name="upload_photo"),
]