from ast import Delete
from rest_framework.views import APIView
from . serializers import *
from rest_framework.response import Response
from rest_framework import status


class Crud(APIView):
    def post(self,request):
        serializer = DemoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("failed")  

      
    def get(self,request,id=None):
        try:
            if id:
                obj = Entry.objects.get(id=id)
                serializer = DemoSerializer(obj)   
            else:
                objs = Entry.objects.all()
                serializer = DemoSerializer(objs,many=True)   
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response("No data",status=status.HTTP_204_NO_CONTENT)    

    def delete(self,request,id=None):
        obj = Entry.objects.get(id=id)
        obj.delete()
        return Response("deleted",status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, id, format=None):
        obj = Entry.objects.get(id=id)
        serializer = DemoSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    





   