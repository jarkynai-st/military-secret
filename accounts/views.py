from django.shortcuts import render
from rest_framework.response import Response
from .serializer import *
from rest_framework import views, viewsets, generics, status


class RegisterView(views.APIView):

    def get(self,request,*args,**kwargs):
        users = User.objects.all()
        serializer = RegisterSerializer(users,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)