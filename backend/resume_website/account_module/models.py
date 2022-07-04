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



class user_work_samples(models.Model):
    post_title = models.CharField(max_length=200, default='', blank=True, null=True)
    post_link = models.CharField(max_length=200, default='', blank=True, null=True)
    post_description = models.TextField()
    image = models.ForeignKey('user_work_samples', on_delete=models.CASCADE, default='', blank=True, null=True)
    post_id = models.CharField(max_length=200, default='', blank=True, null=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User_model, on_delete=models.CASCADE, default='', blank=True, null=True, editable=False)

    def __str__(self):
        return self.post_title


class work_samples_image(models.Model):
    post_image = models.FileField(upload_to='images/work-samples/')
    post_id = models.CharField(max_length=200, default='', blank=True, null=True)
    user = models.ForeignKey(User_model, on_delete=models.CASCADE, default='', blank=True, null=True, editable=False)

    def __str__(self):
        return self.post_id