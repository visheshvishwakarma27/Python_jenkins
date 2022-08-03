from django.shortcuts import render
from app.serializers import PersonSerializer
from .models import Person
# Create your views here.

from rest_framework import viewsets

class PersonView( viewsets.ModelViewSet):
   
    serializer_class = PersonSerializer
    
    
