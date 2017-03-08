from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
CHOICES = [('yeah', 'Will ich machen'),
		   ('ez', 'Kann ich'),
		   ('nope', 'Interessiert mich nicht')]


class Attendee(models.Model):
    '''model for registerd attendees'''
    
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=150)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    submitted_date = models.DateTimeField(default=timezone.now)
    coding_einsteiger = models.CharField(max_length=20, default='nope', choices=CHOICES)
    coding_fortgeschritten = models.CharField(max_length=20, default='nope', choices=CHOICES)
    medien_bearbeitung = models.CharField(max_length=20, default='nope', choices=CHOICES)
    linux = models.CharField(max_length=20, default='nope', choices=CHOICES)
    roboter = models.CharField(max_length=20, default='nope', choices=CHOICES)
    loeten = models.CharField(max_length=20, default='nope', choices=CHOICES)
    elektronik = models.CharField(max_length=20, default='nope', choices=CHOICES)
    wearables = models.CharField(max_length=20, default='nope', choices=CHOICES)
    freitext = models.TextField(blank=True)