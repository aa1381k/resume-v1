from django.urls import path
from .views import datainfo, Get_contact

urlpatterns = [
    path('',datainfo.as_view(), name='dyhome'),
    path('Get_contact/', Get_contact, name='dycontact'),
]