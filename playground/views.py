from django.shortcuts import render
from django.core.mail import EmailMessage, BadHeaderError


def say_hello(request):
    try:
        message = EmailMessage('subject', 'mesage',
                               'from@nik.com', ['random@random.com'])
        message.attach_file('playground/static/images/pepe.jpeg')
        message.send()
    except BadHeaderError:
        pass
    return render(request, 'hello.html', context={'name': 'Nikola'})
