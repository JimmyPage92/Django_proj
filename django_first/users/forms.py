from django.contrib.auth.forms import UserCreationForm, User
from django import forms
from .models import Profile



class UserRegistration(UserCreationForm):
    email = forms.EmailField(label='Provide your email')
    name = forms.CharField(label="Your name", max_length=40)
    surname = forms.CharField(label='Your surname',max_length=40)

    class Meta:
        model = User
        fields = ['name','surname','username', 'email', 'password1' , 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

