from django.shortcuts import render
from rest_framework import generics
from .serializer import CoachSerializer
from .models import CoachModel
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ListCoachViews(generics.ListAPIView):
    queryset = CoachModel.objects.all()
    serializer_class = CoachSerializer
