from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page.as_view(), name='home-page'),
    path('about-us/', views.about_page.as_view(), name='about-page'),
]


