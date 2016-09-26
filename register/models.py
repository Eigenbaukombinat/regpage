from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Attendee(models.Model):
    '''model for registerd attendees'''
    
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=150)
    email = models.EmailField()
    birthdate = models.DateField(default=timezone.now)
    submitted_date = models.DateTimeField(default=timezone.now)
