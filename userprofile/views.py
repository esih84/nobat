from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
# def profile_save(request):
#     if request.method == 'POST':
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         user_profile = UserProfileUpdate(request.POST, instance=request.user.profile)
#         print(user_profile)
#         if user_profile.is_valid() or user_form.is_valid():
#             user_form.save()
#             user_profile.save()
#             # messages.success(request, 'Your profile is updated successfully')
#             return redirect('accounts:profile')
#
#     else:
#         user_form = UserUpdateForm(instance=request.user)
#         user_profile = UserProfileUpdate(instance=request.user.profile)
#     context = {
#         'user_form': user_form,
#         'user_profile': user_profile,
#     }
#     return render(request, 'accounts/update.html', context)
from rest_framework import permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import profile, Create_Services, photo
from .serializers import ProfileSerializer, ProfileUserSerializer, ServicesSerialaizer, PhotoSerialaizer


class create_profile(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        model = profile.objects.all()

        serializer = ProfileSerializer(model, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request, *args, **kwargs):
        serializer = ProfileSerializer(data=request.data, instance=request.user.pr)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class create_profile_user(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        model = profile.objects.all()

        serializer = ProfileUserSerializer(model, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request, *args, **kwargs):
        serializer = ProfileUserSerializer(data=request.data, instance=request.user.pr)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class create_service(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        model = Create_Services.objects.all()

        serializer = ServicesSerialaizer(model, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ServicesSerialaizer(data=request.data,)
        if serializer.is_valid():
            post = Create_Services.objects.create(title=serializer.data['title'], price=serializer.data['price'], user_id=request.user.id )
            post.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class upload_photo(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        model = photo.objects.all()

        serializer = PhotoSerialaizer(model, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = PhotoSerialaizer(data=request.data,)
        if serializer.is_valid():
            post = photo.objects.create(photo=serializer.data['photo'], user_id=request.user.id )
            post.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

