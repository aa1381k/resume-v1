from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs_list.as_view(), name='blogs-page'),
]


