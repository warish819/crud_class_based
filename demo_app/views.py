from django.shortcuts import render
from rest_framework import  viewsets
from rest_framework.viewsets import ModelViewSet
from demo_app.serializers import *
from . models import Entry
from django.contrib.auth.models import User, Group
from rest_framework.views import *

# Create your views here.

class Entry(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = DemoSerializer
    

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer    
    
      
class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
   
    


   

