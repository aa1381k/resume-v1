from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_resume.as_view(), name='create_resume-page'),
    path('savedata/user_base_info/', views.user_base_info_ajax),
    path('savedata/user_social/', views.user_socialmedia_ajax, name='social-media'),
]


