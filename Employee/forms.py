from django.forms import ModelForm
from Employee.models import UserProfile
from django import forms

class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields=["phone","address","imag"]
        widgets={
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),

        }
