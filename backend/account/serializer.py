from .models import CustomUser
from rest_framework import serializers, validators
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate, models


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username', 'email','password',)
        extra_kwargs = {
            'password':{'write_only':True},
            'email':{'required':True,
                    'allow_blank':False,
                    'validators':[
                        validators.UniqueValidator(
                              models.User.objects.all(),'email already exists'
                            )
                    ]  
            }
        }
    
    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = get_user_model().objects.create_user(username = username, email = email, password = password)
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)

    def check_user(self, validated_data):
        user = authenticate(email = validated_data['email'], password = validated_data['password'])
        if not user:
            raise ValidationError('invalid email or password')
        return user
        

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email', 'password',)


