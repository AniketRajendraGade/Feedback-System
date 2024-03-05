from django.db import models

# Create your models here.
class Details(models.Model):
    serial_number=models.CharField(max_length=50)
    Name=models.CharField(max_length=50)
    Phone_number=models.CharField(max_length=10)
    Email=models.EmailField()
    Visit_First_Time=models.BooleanField(default=False)
    Food_You_liked = models.CharField(max_length=20)
    Time_slot=models.CharField(max_length=20)
    Upload_Photo=models.ImageField(upload_to='img/')

    def __str__(self):
        return self.Name