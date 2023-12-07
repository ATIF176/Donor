from django import forms
from .models import DonorRegister  # Import your Register model here

class RegisterForm(forms.ModelForm):
    bgroup = forms.ChoiceField(label='Blood Group', 
                               choices=[('--------------', '--------------'), 
                                        ('A+', 'A+'), ('A-', 'A-'),('B+','B+'),
                                        ('B-','B-'),('O+','O+'),('O-','O-'),
                                        ('AB+','AB+'),('AB-','AB-')], 
                                        widget=forms.Select(attrs={'class':'form-control col-lg-10'}))
    class Meta:
        model = DonorRegister
        fields = ['fname', 'lname', 'email', 'city', 'phone', 'donorid', 'bgroup', 'dob', 'ldonation', 'img','more']
        labels = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'email': 'Email',
            'city': 'Your Residential City',
            'phone': 'Phone Number',
            'donorid': 'Donor ID',
            'more': 'Additional Information',
            'dob': 'Date of Birth',
            'ldonation': 'Last Donation',
            'img': 'Profile Image',
        }

        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control col-lg-10'}),
            'lname': forms.TextInput(attrs={'class': 'form-control col-lg-10 '}),
            'email': forms.EmailInput(attrs={'class': 'form-control col-lg-10'}),
            'city': forms.TextInput(attrs={'class': 'form-control col-lg-10'}),
            'phone': forms.TextInput(attrs={'class': 'form-control col-lg-10'}),
            'donorid': forms.TextInput(attrs={'class': 'form-control col-lg-10'}),
            'more': forms.Textarea(attrs={'class': 'form-control col-lg-10'}),
            'dob': forms.DateInput(attrs={'class': 'form-control col-lg-10'}),
            'ldonation': forms.DateInput(attrs={'class': 'form-control col-lg-10'}),
            'img': forms.FileInput(attrs={'class': 'form-control col-lg-10'}),
        }
