from django import forms
# from .models import Data

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class UserData(forms.ModelForm):
#     class Meta:
#         model  = Data
#         fields = ['amount', 'date', 'description', 'category']

class UserRegistrationForm (UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        #used tuple since we used in build function UserCreationForm