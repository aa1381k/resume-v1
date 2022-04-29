from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_resume.as_view(), name='create_resume-page'),
    path('savedata/user_base_info/', views.user_base_info_ajax),
    path('savedata/user_social/', views.user_socialmedia_ajax, name='social-media'),
    path('savedata/user_lang/', views.user_langurages_ajax, name='langurages'),
    path('savedata/user_skill/', views.user_skills_ajax, name='skills'),
    path('savedata/user_certificate/', views.user_certificate, name='certificate'),
    path('savedata/user_education/', views.user_education_ajax, name='education'),
]


