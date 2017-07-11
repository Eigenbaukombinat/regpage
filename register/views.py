#coding:utf8
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
import datetime
from .models import *
from .forms import *

## mail to send message if someone signed up
MAIL = 'info@junghacker.de'

## mail address shown as sender for mail
SENDER_MAIL = 'info@junghacker.de'

def register(request):
    '''view to handle registerpage'''

    form = AttendeeForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        try:
            age = int(form.cleaned_data['age'])
        except:
            return render(request, 'status.html',{'headline': 'Fehler!', 'status':'Scheinbar hast du kein gueltiges Alter eingegeben.'})
        if age < 10:
            return render(request, 'status.html',{'headline': 'Sorry!', 'status':'Du bist leider noch zu jung. Erst ab 10 Jahren darfst du teilnehmen.'})
        if age > 18:
            return render(request, 'status.html',{'headline': 'Sorry!', 'status':'Du bist leider zu alt. Teilnehmen darfst du, solange du noch 18 Jahre alt bist.'})

            
        attendee = Attendee()
        attendee.firstname = form.cleaned_data['firstname']
        attendee.lastname = form.cleaned_data['lastname']
        attendee.email = form.cleaned_data['email']
        attendee.age = form.cleaned_data['age']
        attendee.coding_einsteiger = form.cleaned_data['coding_einsteiger']
        attendee.coding_fortgeschritten = form.cleaned_data['coding_fortgeschritten']
        attendee.medien_bearbeitung = form.cleaned_data['medien_bearbeitung']
        attendee.linux = form.cleaned_data['linux']
        attendee.roboter = form.cleaned_data['roboter']
        attendee.loeten = form.cleaned_data['loeten']
        attendee.elektronik = form.cleaned_data['elektronik']
        attendee.wearables = form.cleaned_data['wearables']
        attendee.freitext =form.cleaned_data['freitext']
        attendee.submitted_date = datetime.datetime.now()
       
        submitted = attendee.submitted_date.ctime()
        message ='Ein neuer Teilnehmer hat sich am ' + submitted + ' angemeldet. Name: ' + attendee.firstname + ' ' + attendee.lastname + ' Email: ' + attendee.email + ' Alter: %i' % attendee.age  
        message += '''

Umfrage:
        
coding_einsteiger: ''' + attendee.coding_einsteiger + '''
coding_fortgeschritten: ''' + attendee.coding_fortgeschritten + '''
medien_bearbeitung: ''' + attendee.medien_bearbeitung + '''
linux: ''' + attendee.linux + '''
roboter: ''' + attendee.roboter + '''
loeten: ''' + attendee.loeten + '''
elektronik: ''' + attendee.elektronik + '''
wearables: ''' + attendee.wearables + '''

freitext:
''' + attendee.freitext
        try:
            send_mail(
                'Deine Anmeldung zu JUNGHACKER - Programmieren fuer Kids',
                u'''Liebe(r) %s,

Deine Registrierung für {JUNGHACKER} - Programmieren für Kids 
am 22. Juli 2017 war erfolgreich! Wir werden uns in den nächsten 
Wochen bei dir melden und dir deine Teilnahme bestätigen. Falls wir 
zu viele Anmeldungen bekommen, werden wir leider nicht alle 
berücksichtigen können.


Liebe Grüße, 

Dein Team von {JUNGHACKER} – Programmieren für Kids.
''' % attendee.firstname,
                    SENDER_MAIL,
                    [attendee.email],
                    fail_silently=False,
                    )
            send_mail(
                    'JUNGHACKER anmeldung',
                    message,
                    SENDER_MAIL,
                    [MAIL],
                    fail_silently=False,
                    )
        except:
            pass
            #return render(request, 'status.html',{'headline': 'Schwerer Fehler!', 'status':'Es ist etwas schiefgegangen. Bitte versuche es später noch einmal oder melde dich unter info@junghacker.de!'})
            
        attendee.save()
        return render(request, 'status.html', {'headline': 'Danke fuer deine Anmeldung!', 'status':'Eine Bestätigungsmail wurde an deine E-Mail Adresse geschickt.'})
            
    form = AttendeeForm()
    return render(request, 'register_page.html', {'form':form})
