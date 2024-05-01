from django.db import models

# Create your models here.
class  Reservation(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    date=models.DateField()
    number=models.IntegerField()
    message=models.TextField()
    def __str__(self):
        return self.name
        
