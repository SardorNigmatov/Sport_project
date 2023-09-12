from django.shortcuts import render
from rest_framework.views import APIView
from .models import YangilikModels, Gyms , CoachModel
from .serializers import YangilikSerializer, GymsSerializer, GymsCreateSerializer , CoachSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_201_CREATED
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
# Create your views here.


class AllYangilikView(generics.ListAPIView):
    queryset = YangilikModels.objects.all()
    serializer_class = YangilikSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        user=self.request.user
        return YangilikModels.objects.filter(user=user)


class DetailYangilikView(APIView):
    def get(self, request, *args, **kwargs):
        yangilik = get_object_or_404(YangilikModels, id=kwargs['yangilik_id'])
        serializer = YangilikSerializer(yangilik)
        return Response(serializer.data)



class CreatYangilikView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = YangilikSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.errors)


class UpdateYangilikView(APIView):
    def patch(self, request, *args, **kwargs):
        yangilik = get_object_or_404(YangilikModels, id=kwargs['yangilik_id'])
        serializer = YangilikSerializer(yangilik, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DeleteYangilikView(APIView):
    def delete(self, request, *args, **kwargs):
        yangilik = get_object_or_404(YangilikModels, id=kwargs['yangilik_id'])
        yangilik.delete()
        return Response({'msg': 'deleted'})


# Create your views here.

class CoachListViews(generics.ListAPIView):
    queryset = CoachModel.objects.all()
    serializer_class = CoachSerializer

class CoachCreateViews(generics.CreateAPIView):
    queryset = CoachModel.objects.all()
    serializer_class = CoachSerializer
    permission_classes = (IsAuthenticated,)

    
class CoachUpdateViews(generics.UpdateAPIView):
    queryset = CoachModel.objects.all()
    serializer_class = CoachSerializer
    permission_classes = (IsAuthenticated,)

class CoachDeleteViews(generics.DestroyAPIView):
    queryset = CoachModel.objects.all()
    serializer_class = CoachSerializer
    permission_classes = (IsAuthenticated,)


class GymsListView(generics.ListAPIView):
    queryset = Gyms.objects.all()
    serializer_class = GymsSerializer


class GymsDetailView(generics.RetrieveAPIView):
    queryset = Gyms.objects.all()
    serializer_class = GymsSerializer

class GymsCreateView(generics.CreateAPIView):
    queryset = Gyms.objects.all()
    serializer_class = GymsCreateSerializer

class GymsUpdateView(generics.UpdateAPIView):
    queryset = Gyms.objects.all()
    serializer_class = GymsSerializer

class GymsDeleteView(generics.DestroyAPIView):
    queryset = Gyms.objects.all()
    serializer_class = GymsSerializer



