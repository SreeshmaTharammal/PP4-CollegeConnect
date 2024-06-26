from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from .choices import NATIONALITY_CHOICES

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    nationality = forms.ChoiceField(choices=NATIONALITY_CHOICES)

    class Meta:
        model = UserProfile
        fields = ['address', 'phone_number', 'emergency_contact_number', 'nationality', 'is_student', 'is_instructor', 'is_admin', 'is_guest']
