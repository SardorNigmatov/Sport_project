from rest_framework.serializers import ModelSerializer
from .models import CoachModel

class CoachSerializer(ModelSerializer):
    class Meta:
        model = CoachModel
        fields = ('full_name','degree','image')