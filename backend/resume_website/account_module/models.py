from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class User_model(AbstractUser):
    phone = models.CharField(max_length=300, default='', blank=True, null=True)
    avatar = models.ImageField(upload_to='images/user-profile', blank=True, null=True, default=None)
    email_active_code = models.CharField(max_length=300, blank=True, null=True, default=None)
    bg_image = models.ImageField(upload_to='images/user-profile', blank=True, null=True)
    theme_color = models.CharField(max_length=200, blank=True, null=True, default='blue')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


    def get_full_name(self):
        return self.first_name + " " + self.last_name
