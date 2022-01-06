from django.db import models

# Create your models here.


class Book(models.Model):
    book_name=models.CharField(max_length=120,unique=True)
    author=models.CharField(max_length=120)
    copies=models.PositiveIntegerField(default=5)
    price=models.IntegerField()
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.book_name

#create
#


# shell=> python3 manage.py shell
#CRUD(create,retrive,updare,delete)

# ORM querirs

# orm query for creating an object
#refname=ModelName(field1=value,field2=vale,,,,,,)
#ref.save()

#book=Book(book_name='alchemist',author='paulo',copies=50,price=500)
#book.save()
from django.contrib.auth.models import User