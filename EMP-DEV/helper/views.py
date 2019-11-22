from django.shortcuts import render, HttpResponse
from django.core.mail import EmailMessage

def sendEmail(request):
    mail_body = '<h1>This is fris email from Django!</h1>'
    msg = EmailMessage("Welcome Anvesh", mail_body, 
            'pythonic.style@gmail.com', ['anvesh.balija@gmail.com',
             'narendranaru45@gmail.com'])
    msg.content_subtype = "html"
    msg.send()

    return HttpResponse("Mail sent successfully!")
