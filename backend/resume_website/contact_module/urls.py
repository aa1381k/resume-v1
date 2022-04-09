from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_page.as_view(), name='contact-page'),
]


