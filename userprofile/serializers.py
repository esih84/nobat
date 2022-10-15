from .models import *
from rest_framework import serializers
from django.contrib.auth import get_user_model


class ProfileSerializer(serializers.ModelSerializer):
    # photo = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=False,  use_url=True, required=False)
    class Meta:
        model = profile
        fields = ['first_name', 'last_name', 'phone', 'city', 'address', 'photo']


class ProfileUserSerializer(serializers.ModelSerializer):
    # photo = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=False,  use_url=True, required=False)
    class Meta:
        model = profile
        fields = ['first_name', 'last_name', 'phone', 'city', 'photo']


class ServicesSerialaizer(serializers.ModelSerializer):
    # photo = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=False,  use_url=True, required=False)
    class Meta:
        model = Create_Services
        fields = ['title', 'price']


class PhotoSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = photo
        fields = ['photo']
