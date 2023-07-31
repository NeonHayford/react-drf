from django.contrib.auth import login, logout
from rest_framework.views import APIView
from .serializer import *
from rest_framework.status import *
from rest_framework import permissions
from rest_framework.response import Response 
from rest_framework.authentication import SessionAuthentication
# from knox.models import AuthToken
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token


# Create your views here.
class signupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        # try:
            serializer = RegisterSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                user = User.objects.filter(id)
                token = Token.objects.create(user)
                token = token.key
                if user:
                    return Response({
                        'token': token,
                        'user' : serializer.data
                    },
                    status = HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
            return Response(serializer.errors)
        # except Exception as e:
        #     return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)
        

class loginView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    def post(self, request):
        try:
            serializer = LoginSerializer(data = request.data)
            serializer.is_valid(raise_exception = True)
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(email=email, password=password)
            if user is None:
                raise AuthenticationFailed('Invalid credentials')
            token = RefreshToken.for_user(user)
            data = {
                'tokens': {
                    'refresh': str(token),
                    'access': str(token.access_token)
                }
            }
            return Response(data, status=HTTP_200_OK)
        except AuthenticationFailed as e:
            return Response({'error': str(e)}, status=HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'status': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        


    # def post(self, request):
    #     try:
            # serializer = LoginSerializer(data = request.data)
            # if serializer.is_valid():
            #     email = serializer.data['email']
            #     password = serializer.data['password']
            #     user = authenticate(email = email, password = password)
            #     token = RefreshToken.for_user(user)
            #     data = {
            #         'tokens': {
            #             'refresh': str(token),
            #             'access': str(token.access_token)
            #         }
            #     }
        #     email = request.data['email']
        #     password = request.data['password']
        #     user = User.objects.filter(email=email).first()
        #     if user is None:
        #         raise AuthenticationFailed('User not found')
        #     if not user.check_password(password):
        #         return AuthenticationFailed('User password is incorrect')
        #     return Response({'id': user.id, 'username': user.username, 'password': user.password})
        #         # login(request, user)
        #         # return Response(data, status = HTTP_202_ACCEPTED)
        # except Exception as e:
        #     return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)


class logoutView(APIView):
    def post(self, request):
        try:
            logout(request)
            return Response(status = HTTP_200_OK)
        except Exception as e:
            return Response({'status': str(e)}, status = HTTP_405_METHOD_NOT_ALLOWED)
        

class userView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        try:
            serializer = UserSerializer(data = request.user)
            serializer.is_valid(raise_exception = True)
            return Response(serializer.data, status = HTTP_200_OK)
        except:
            return Response(serializer.errors, status = HTTP_405_METHOD_NOT_ALLOWED)

# class CartView(APIView):
#     def get(self, request):
#         cart = CustomUser.objects.all()
#         serializer = UserSerializer(cart, many=True)
#         return Response(serializer.data)
