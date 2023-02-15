from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view.as_view(), name='register-page'),
    path('login/', views.Login.as_view(), name='login-page'),
    path('logout/', views.Loguot.as_view(), name='logout-page'),
    path('forgetpass/', views.Forgotpassword.as_view(), name='forgot-page'),
    path('profile/', views.profile_view.as_view(), name='profile-page'),
    path('resetpass/<active_code>', views.Resetpassword.as_view(), name='resetpass-page'),
    path('active-account/<active_code>', views.activate_account.as_view(), name='active-account-page'),
    path('add_work_samples/', views.add_work_samples.as_view(), name='add_work_samples_post'),
    path('user_work_samples/work_samples_images/', views.work_samples_images, name='work_samples_images'),
    path('<username>', views.users_profile.as_view(), name='users_profile'),
]


