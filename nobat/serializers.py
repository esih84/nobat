from rest_framework import serializers
from .models import MyUser
from django.contrib.auth import authenticate


# class CreateUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MyUser
#         fields = ('email', 'username', 'password')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         user = MyUser.objects.create_user(validated_data['username'],
#                                           validated_data['email'],
#                                           validated_data['password'])
#         return user


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = MyUser
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = MyUser(email=self.validated_data['email'], username=self.validated_data['username'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user
