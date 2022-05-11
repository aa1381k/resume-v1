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
    path('savedata/user_job/', views.user_job_ajax, name='job'),
    path('savedata/user_project/', views.user_projects_ajax, name='project'),
    path('savedata/user_internship/', views.user_internship_ajax, name='internship'),
    path('savedata/user_introduced/', views.user_introduced_ajax, name='introduced'),
    path('savedata/user_entertainment/', views.user_entertainment_ajax, name='entertainment'),
    path('savedata/resume_remove_item/', views.resume_remove_item, name='resume_remove_item'),
]


