from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.status import *

# Create your views here.
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
