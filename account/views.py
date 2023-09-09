from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializer import CustomUserSerializer

class SignUpUserViews(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
