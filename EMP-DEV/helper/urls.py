from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^send_email/', views.sendEmail, name="send_email")
]