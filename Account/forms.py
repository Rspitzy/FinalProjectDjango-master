from django import forms
from .models import Profile
from django.contrib.auth.models import User


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True)


    class Meta:
        model = User
        fields = ['username']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number',)