from django.db import models

# Create your models here.





class CoachModel(models.Model):
    full_name = models.CharField(max_length=50, default='')
    degree = models.CharField(max_length=150, default='')
    image = models.ImageField(upload_to='coach/',blank=True, null=True)
    
    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        db_table = 'coach'
    