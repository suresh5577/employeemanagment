from django.core.mail import EmailMessage
from django.conf import settings
import base64
import urllib

def sendEmail(mail_subject, to_email_ids, mail_body):
    try:
        msg = EmailMessage(mail_subject, mail_body, 
                settings.FROM_EMAIL_ID, to_email_ids)
        msg.content_subtype = "html"
        msg.send()
    except:
        return False
    return True


def encrypt(text):
    try:
        #convert text into base64 encode format
        enc_text = base64.b64encode(text.encode('ascii'))

        #convert base64 encode enc_text into url encode
        enc_text = urllib.parse.quote(enc_text)
        return enc_text
    except:
        pass

def decrypt(enc_text):
    try:
        text = urllib.parse.unquote(enc_text)
        text = base64.b64decode(text)
        text = text.decode("utf-8")
        return text
    except:
        pass