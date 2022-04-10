from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view.as_view(), name='register-page'),
    path('login/', views.Login.as_view(), name='login-page'),
    path('active-account/<active_code>', views.activate_account.as_view(), name='active-account-page'),
]


