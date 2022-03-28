from django import forms
from django.forms import ModelForm
from owner.models import Employees
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Employee.models import UserProfile

class EmployeeForm(ModelForm):
    class Meta:
        model=Employees
        # fields=["Employee_name","Email","password","phone","address"]
        fields="__all__"
        widgets={
            "Employee_name":forms.TextInput(attrs={"class":"form-control"}),
            "Email":forms.EmailInput(attrs={'class':"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
            "phone":forms.TextInput(attrs={"class": "form-control"}),
            "address":forms.TextInput(attrs={"class": "form-control"}),

        }



# class BookForm(forms.Form):
#     book_name=forms.CharField()
#     author=forms.CharField()
#     price=forms.IntegerField()
#     copies=forms.IntegerField()
#
#     def clean(self):
#         cleaned_data=super().clean()
#         price=cleaned_data["price"] #-50
#         copies=cleaned_data["copies"] #-40
#         if price<0:
#             msg="invalid price"
#             self.add_error("price",msg)
#         if copies<0:
#             msg="invalid copies"
#             self.add_error("copies",msg)
#
# class BookChangeForm(forms.Form):
#     book_name = forms.CharField()
#     author = forms.CharField()
#     price = forms.IntegerField()
#     copies = forms.IntegerField()
#
#     def clean(self):
#         cleaned_data = super().clean()
#         price = cleaned_data["price"]  # -50
#         copies = cleaned_data["copies"]  # -40
#         if price < 0:
#             msg = "invalid price"
#             self.add_error("price", msg)
#         if copies < 0:
#             msg = "invalid copies"
#             self.add_error("copies", msg)
#
#

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["email","username","password1","password2"]
        widgets={
            "email":forms.EmailInput(attrs={'class':"form-control"}),
            "username":forms.TextInput(attrs={"class": "form-control"}),
            "password1":forms.CharField(max_length=15,widget=(forms.PasswordInput(attrs={"class":"form-control","placeholder":"type password"}))),
            "password2": forms.CharField(max_length=15, widget=(forms.PasswordInput(attrs={"class": "form-control", "placeholder": "type password"}))),
        }





class SigninForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))





# class UserRegistrationForm(UserCreationForm):
#     class Meta:
#         model=Employees
#         fields="__all__"
#         widgets = {
#             "Employee_name": forms.TextInput(attrs={"class": "form-control"}),
#             "Email": forms.EmailInput(attrs={'class': "form-control"}),
#             "password": forms.PasswordInput(attrs={"class": "form-control"}),
#             "phone": forms.TextInput(attrs={"class": "form-control"}),
#             "address": forms.TextInput(attrs={"class": "form-control"}),
#
#         }


