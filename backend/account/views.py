from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.status import *

# Create your views here.
# class ChangePasswordView(APIView):
#     def post(self, request, *args, **kwargs):
#         try:
#             serializer = ChangePasswordSerializer(request.data)
#             if serializer.is_valid(raise_exception=True):
#                 return Response({'status': 'Password Reset successfully...'}, status=HTTP_202_ACCEPTED)
#             return Response(serializer.error_messages, status=HTTP_401_UNAUTHORIZED)
#         except Exception as e:
#             return Response({'status': str(e)}, status=HTTP_403_FORBIDDEN)
#         pass

class resetpassword(APIView):
    def post(self,request):
        serializer=ChangePasswordSerializer(data=request.data)
        alldatas={}
        if serializer.is_valid(raise_exception=True):
            name=serializer.save()
            alldatas['data']="successfully registered"
            print(alldatas)
            return Response(alldatas)
        return Response('failed retry after some time')

        # class logout(APIView):
        # def get(self,request):
        # request.user.auth_token.delete()
        # auth.logout(request)
        # return Response(“successfully deleted”)
