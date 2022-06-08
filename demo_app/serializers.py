from dataclasses import field, fields
from rest_framework import serializers
from demo_app.models import Entry
from django.contrib.auth.models import User, Group



class DemoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Entry
        fields= ['id','name','address']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields= '__all__'
        include = 'url'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Group
        fields = '__all__'
        include = 'url'
                              
           