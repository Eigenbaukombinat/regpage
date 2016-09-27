from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
import datetime
from .models import *
from .forms import *

## mail to send message if someone signed up
MAIL = 'example@example.com'

## mail address shown as sender for mail
SENDER_MAIL = 'sender@example.com'

def register(request):
    '''view to handle registerpage'''

    if request.method == 'POST':
        form = AttendeeForm(request.POST)
        if form.is_valid():
            
            try:
               attendee = Attendee.objects.get(email=form.cleaned_data['email'])
               return render(request, 'status.html',{'status':'Diese Emailadresse wird bereits verwendet!'})
            except: 
            
                attendee = Attendee()
                attendee.firstname = form.cleaned_data['firstname']
                attendee.lastname = form.cleaned_data['lastname']
                attendee.email = form.cleaned_data['email']
                attendee.birthdate = form.cleaned_data['birthdate']
                attendee.submitted_date = datetime.datetime.now()
                
                submitted = attendee.submitted_date.ctime()
                birth = attendee.birthdate.isoformat()
                message ='Ein neuer Teilnehmer hat sich am ' + submitted + ' angemeldet. Name: ' + attendee.firstname + ' ' + attendee.lastname + ' Email: ' + attendee.email + ' Geburtstag: ' + birth    

            try:
                send_mail(
                    'Hackaday 2016 Anmeldung',
                    'Deine Registrierung für den Hackaday 2016 war erfolgreich!',
                    SENDER_MAIL,
                    [attendee.email],
                    fail_silently=False,
                    )
                send_mail(
                    'Hackaday 2016 Anmeldung',
                    message,
                    SENDER_MAIL,
                    [MAIL],
                    fail_silently=False,
                    )
            except BadHeaderError:
                return render(request, 'status.html',{'status':'Invalid header found!'})
            except:
                return render(request, 'status.html',{'status':'Something went wrong!'})
            
            attendee.save()
            return render(request, 'status.html', {'status':'success'})
            
    form = AttendeeForm()
    return render(request, 'register_page.html', {'form':form})
