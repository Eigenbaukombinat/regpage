from django import forms
from .models import *

class AttendeeForm(forms.ModelForm):
    '''form for Attendee model'''
    
    class Meta:
        model = Attendee
        fields = ['firstname','lastname','email','birthdate',]
        widgets = {
            'firstname': forms.TextInput(attrs={'class':'form-control input-sm', 'placeholder':'Vorname'}),
            'lastname': forms.TextInput(attrs={'class':'form-control input-sm', 'placeholder':'Nachname'}),
            'email': forms.EmailInput(attrs={'class':'form-control input-sm', 'placeholder':'Emailadresse'}),
            'birthdate': forms.DateInput(attrs={'class':'form-control input-sm', }),
        }
        
