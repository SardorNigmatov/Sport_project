from django.shortcuts import render
from rest_framework import generics
from .serializer import CoachSerializer
from .models import CoachModel
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class CoachListViews(generics.ListAPIView):
    queryset = CoachModel.objects.all()
    serializer_class = CoachSerializer

class CoachCreateViews(generics.CreateAPIView):
    queryset = CoachModel.objects.all()
    serializer_class = CoachSerializer
    # permission_classes = (AutherUserPermissions,)

    
class CoachUpdateViews(generics.UpdateAPIView):
    queryset = CoachModel.objects.all()
    serializer_class = CoachSerializer
    # permission_classes = (AdminPermission,)

class CoachDeleteViews(generics.DestroyAPIView):
    queryset = CoachModel.objects.all()
    serializer_class = CoachSerializer
    # permission_classes = (AdminPermission,)
    