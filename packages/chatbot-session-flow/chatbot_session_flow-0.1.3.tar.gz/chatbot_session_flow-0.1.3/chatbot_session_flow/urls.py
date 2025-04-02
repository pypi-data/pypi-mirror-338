from django.urls import re_path
from app import views
from .views import *

urlpatterns = [
    re_path('sendTestMessage', views.sendWhatsappMessageViaNgumzo),
    re_path('messageCallback', views.messageCallback),
]
