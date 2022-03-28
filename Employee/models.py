from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    phone=models.CharField(max_length=12,unique=True)
    address=models.CharField(max_length=120)
    imag=models.ImageField(upload_to="images", null=True, blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="employee")






