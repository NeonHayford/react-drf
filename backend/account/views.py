from django.contrib.auth import get_user_model, login, logout
from rest_framework.views import APIView
from .serializer import *
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED, HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK, HTTP_202_ACCEPTED
from rest_framework import permissions
from rest_framework.response import Response 
from rest_framework.authentication import SessionAuthentication
# from knox.models import AuthToken
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
class signupView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, *args, **kwargs):
        try:
            serializer = RegisterSerializer(data = request.data)
            if serializer.is_valid(raise_exception = True):
                user = serializer.create(request.data)
                token = RefreshToken.for_user(user)
                data = serializer.data
                if user:
                    data['tokens'] = {'refresh': str(token), 'access': str(token.access_token)}
                    return Response(data, status = HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status = HTTP_405_METHOD_NOT_ALLOWED)
            return Response(serializer.errors)
        except Exception as e:
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)
        

class loginView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    def post(self, request):
        try:
            serializer = LoginSerializer(data = request.data)
            if serializer.is_valid():
                email = serializer.data['email']
                password = serializer.data['password']
                user = authenticate(email = email, password = password)
                token = RefreshToken.for_user(user)
                data = {
                    'tokens': {
                        'refresh': str(token),
                        'access': str(token.access_token)
                    }
                }
                login(request, user)
                return Response(data, status = HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)


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