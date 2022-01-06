from django import forms
from django.forms import ModelForm
from owner.models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookForm(ModelForm):
    class Meta:
        model=Book
        # fields=["book_name","copies","author","price"]
        fields="__all__"
        widgets={
            "book_name":forms.TextInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={'class':"form-control"}),
            "copies":forms.NumberInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"})
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
        fields=["first_name","last_name","email","username","password1","password2"]


class SigninForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


