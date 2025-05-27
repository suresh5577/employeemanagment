from django.urls import path
from . import views


urlpatterns = [
    path('send_email/', views.sendEmail, name="send_email")
]