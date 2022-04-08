from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_page.as_view(), name='register-page'),
    # path('about-us/', views.about_page.as_view(), name='about-page'),
]


