#coding:utf8
from django import forms
from .models import *

class AttendeeForm(forms.ModelForm):
    '''form for Attendee model'''
    
    class Meta:
        model = Attendee
        fields = ['firstname','lastname','email','age',
                  'coding_einsteiger', 
                  'coding_fortgeschritten',
                  'medien_bearbeitung',
                  'linux',
                  'roboter',
                  'loeten',
                  'elektronik',
                  'wearables',
                  'freitext']
        widgets = {
            'firstname': forms.TextInput(attrs={'class':'form-control input-sm', 'placeholder':'Vorname'}),
            'lastname': forms.TextInput(attrs={'class':'form-control input-sm', 'placeholder':'Nachname'}),
            'email': forms.EmailInput(attrs={'class':'form-control input-sm', 'placeholder':'Emailadresse'}),
            'age': forms.TextInput(attrs={'class':'form-control input-sm', }),
            'coding_einsteiger': forms.RadioSelect(),
            'coding_fortgeschritten': forms.RadioSelect(),
            'medien_bearbeitung': forms.RadioSelect(),
            'linux': forms.RadioSelect(),
            'roboter': forms.RadioSelect(),
            'loeten': forms.RadioSelect(),
            'elektronik': forms.RadioSelect(),
            'wearables': forms.RadioSelect(),
            'freitext': forms.Textarea(attrs={
                'class':'form-control input-sm', 'placeholder':'Platz für weitere Wünsche, Anregungen und Kritik…'}),
        }
        
