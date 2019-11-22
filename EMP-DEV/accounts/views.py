from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.urls import reverse
import base64
import urllib
from django.conf import settings
from helper.utils import encrypt, decrypt, sendEmail
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


def signUp(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            #set user is_active to False
            username = form.cleaned_data.get('username')
            userObj = User.objects.get(username=username)
            userObj.is_active = False
            userObj.save()

            print(username)

            #convert username into base64 encode format
            enc_username = base64.b64encode(username.encode('ascii'))
            print(enc_username)

            #convert base64 encode username into url encode
            enc_username = urllib.parse.quote(enc_username)
            print(enc_username)           



            mail_body = '<h1>Welcome to our Application!!!</h1>'
            mail_body += 'Please click on below link to verify your email account !!!<br /><br /><hr />'
            mail_body += '<a href="%s%s">Verify My Account</a>' % (settings.BASE_DOMAIN, reverse('verify_email', kwargs={'enc_username': enc_username}))
            mail_obj = EmailMessage("Pythonic.Style Verify Your Email 12.17 PM",
                        mail_body, 'pythonic.style@gmail.com', [username])
            mail_obj.content_subtype = 'html'
            mail_obj.send()

            return redirect(reverse('login'))
    
    form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})

def verifyEmail(request, enc_username):
    username = urllib.parse.unquote(enc_username)
    username = base64.b64decode(username)
    username = username.decode("utf-8")

    userObj = User.objects.get(username=username)
    userObj.is_active = True
    userObj.save()

    return redirect(reverse('login'))

def forgotPassword(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)

        try:
            #verify user is exists or throw an error in except block
            User.objects.get(username=username)
            enc_username = encrypt(username)

            mail_subject = "Reset Your Password!!!"
            to_email_ids = [username]
            mail_body = "<h2>If have you requested for password reset? then Please click on below link</h2>"
            mail_body += '<a href="%s%s">Reset Password</a>' % (settings.BASE_DOMAIN, reverse('reset_password', kwargs={'enc_username': enc_username}))

            response = sendEmail(mail_subject, to_email_ids, mail_body)

            if response:
                return HttpResponse("Reset Password link sent to your Email ID ")
            else:
                return HttpResponse("Something went wrong, Please try again later.")
            
        except ObjectDoesNotExist:
            return HttpResponse('User Not Found <br /> <a href="%s">Go Back</a>' % reverse('forgot_password'))

        return redirect(reverse('login'))

    return render(request, 'forgotPassword.html')

def resetPassword(request, enc_username):
    username = decrypt(enc_username)
    try:
        userObj = User.objects.get(username=username)
    except ObjectDoesNotExist:
        raise Http404


    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return HttpResponse("Password and Confirm Password are not matching!!!")
        
        userObj.set_password(password1)
        userObj.save()
        return HttpResponse("Your password reset successfully, <a href='%s'>Go To Login</a>" % reverse('login'))
    
    return render(request, 'resetPassword.html', {'username':username})



