from django.contrib.auth import login
from django.shortcuts import render
from knox.views import LoginView as KnoxLoginView
# Create your views here.

from rest_framework.views import APIView

from .serializers import *
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)




class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
