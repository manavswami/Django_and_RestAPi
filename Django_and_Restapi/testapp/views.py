
# Create your views here.
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from testapp.models import global_database
from testapp.serializer import global_databaseSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_jwt.authentication import JSONWebTokenAuthentication



class global_databaseListAPIView(ListAPIView):
    authentication_classes=[JSONWebTokenAuthentication] 
    permission_classes=[IsAuthenticated,]  
    queryset=global_database.objects.all()
        
    serializer_class=global_databaseSerializer
    search_fields=('Phone_Number','Name',)
   
    ordering_fields=('Phone_Number','Name',)




class global_databaseCRUD(ModelViewSet):
    queryset=global_database.objects.all()
        
    serializer_class=global_databaseSerializer
