from .models import *
from rest_framework import serializers
# Adding support
from djoser.serializers import UserCreateSerializer
from django.contrib.auth.models import User


class RegisterSerialiser(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        
        fields = ['id', 'first_name', 'last_name', 'email', 'password']



class ChangePasswordSerializer(serializers.Serializer):
    password  = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only = True)
    password_confirmation  = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only = True)

    class Meta:
        fields = ['password', 'password_confirmation']

    # def validate(self, attrs):
    #     password = attrs.get('password')
    #     password2 = attrs.get('password_confirmation')
    #     user = self.context.get('user')
    #     if password != password2:
    #         raise serializers.ValidationError('Password and confirm password are not the same...')
    #     user.set_password(password)
    #     user.save()
    #     # pass
    #     return attrs