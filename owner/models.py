from django.db import models

# Create your models here.
class Employees(models.Model):
    Employee_name=models.CharField(max_length=120,unique=True)
    Email=models.EmailField()
    password=models.CharField(max_length=50)
    phone=models.IntegerField()
    address = models.CharField(max_length=50)
    photo=models.ImageField(upload_to="images",null=True,blank=True)

    def __str__(self):
        return self.Employee_name
