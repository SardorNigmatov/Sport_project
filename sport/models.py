from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.


class YangilikModels(models.Model):
    Y_nomi = models.CharField(default='', max_length=150)
    Y_matni = models.CharField(max_length=1300, default='')
    Y_vaxti = models.DateField(default=datetime.now)
    Y_rasmi = models.ImageField(upload_to='news/',blank=True,null=True)
    def __str__(self) -> str:
        return self.Y_nomi

    class Meta:
        db_table = 'yangilik'


# Create your models here.



class CoachModel(models.Model):
    full_name = models.CharField(max_length=50, default='')
    degree = models.CharField(max_length=150, default='')
    image = models.ImageField(upload_to='coach/',blank=True, null=True)
    
    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        db_table = 'coach'


class Gyms(models.Model):
    region = models.CharField(max_length=100)
    coach = models.ForeignKey(CoachModel,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gyms',blank=True,null=True)
    trener_phone = models.CharField(max_length=13,default='')


    def __str__(self):
        return self.region

    class Meta:
        db_table = 'gyms'
    