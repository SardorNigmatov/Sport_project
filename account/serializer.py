from rest_framework.serializers import ModelSerializer
from .models import CustomUser
from rest_framework import serializers

class CustomUserSerializer(ModelSerializer):
    password = serializers.CharField(write_only =True)
    
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','phone','email','password')
    def create(self, validated_date):
        user = CustomUser(
            username = validated_date['username'],
            first_name = validated_date['first_name'],
            last_name = validated_date['last_name'],
            phone = validated_date['phone'],
            email = validated_date['email'],
            password = validated_date['password'],
        )
        user.set_password(validated_date['password'])
        user.save()
        return user
    # def end