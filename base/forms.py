from django import forms
from .models import DonorRegister  # Import your Register model here

class RegisterForm(forms.ModelForm):
    class Meta:
        model = DonorRegister
        
        fields = ['fname', 'lname', 'email', 'city', 'phone', 'donorid', 'bgroup', 'more', 'dob', 'img']
