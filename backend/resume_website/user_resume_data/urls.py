from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_resume.as_view(), name='create_resume-page'),
    path('savedata/', views.user_base_info_ajax),
]


