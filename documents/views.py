from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import permissions
from .serializer import *
from .permission import IsSuperuserOrReadOnly

class DocumentView(views.APIView):

    permission_classes = [IsSuperuserOrReadOnly]
    def get(self,request,*args,**kwargs):
        try:
            group = request.user.groups.all()[0].name.lower()
        except IndexError:
            return Response("Please authorize!")
        if group == 'general':
            docs = Document.objects.all()
        elif group == 'geft':

            docs = Document.objects.filter(status='active',secret_level='private')

        elif group in ['sergent','leit','captain']:
            docs = Document.ojects.filter(status='active',secret_level__in=['public','private','secret'])

        elif group in ['major', 'podpol', 'polkovnik']:
            docs = Document.objects.filter(status='active',secret_level__in=['public', 'private', 'secret', 'top-secret'])

        elif group == 'cleaner':
            docs = Document.objects.filter(status='active')

        serializers = DocumentSerializer(docs,many=True)
        return Response(serializers.data)

    def post(self,request,*args,**kwargs):
        serializers = DocumentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"data":"Document created successfully, your grace!"})
        return Response(serializers.errors)
