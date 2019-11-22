from django.conf.urls import url, include
from django.urls import path
from . import views


urlpatterns = [
    path('sign_up/', views.signUp, name='sign_up'),
    path('verify_email/<enc_username>', views.verifyEmail, name='verify_email'),
    path('forgot_password/',views.forgotPassword, name='forgot_password'),
    path('reset_password/<enc_username>', views.resetPassword, name="reset_password")
]