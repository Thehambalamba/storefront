from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError


def say_hello(request):
    try:
        mail_admins('subject', 'mesage', html_message='message')
        # send_mail('subject', 'message',
        #          'info@nikperv.com', ['bob@nikperv.com '])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', context={'name': 'Nikola'})
