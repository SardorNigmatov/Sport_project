from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.


class YangilikModels(models.Model):
    Y_nomi = models.CharField(default='', max_length=150)
    Y_matni = models.CharField(max_length=1300, default='')
    Y_vaxti = models.DateField(default=datetime.now)
    Y_rasmi = models.ImageField(blank=True,null=True)
    def __str__(self) -> str:
        return self.Y_nomi

    class Meta:
        db_table = 'yangilik'


# Create your models here.
