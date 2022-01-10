from django.forms import ModelForm
from customer.models import UserProfile

class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields=["phone","address"]