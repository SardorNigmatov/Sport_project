from rest_framework import serializers
from .models import YangilikModels
from .models import CoachModel
from .models import Gyms

class YangilikSerializer(serializers.ModelSerializer):
    class Meta:
        model = YangilikModels
        fields = ('Y_nomi','Y_matni','Y_vaxti','Y_vaxti','Y_rasmi')


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoachModel
        fields = ('full_name','degree','image')

class GymsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gyms
        fields = ('region','image')

class GymsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gyms
        fields = ('region','coach','trener_phone','image')

