from django.db import models
from account_module.models import User_model
# Create your models here.

MILITARY_CHOICES = (
    ("0", ""),
    ("1", "مشمول"),
    ("2", "در حال خدمت"),
    ("3", "پایان خدمت"),
    ("4", "معاف"),
    ("5", "معافیت تحصیلی"),
    ("6", "معافیت پزشکی"),
    ("7", "معافیت غیر پزشکی"),
)

MARRIED_CHOICES = (
    ("0", ""),
    ("1", "مجرد"),
    ("2", "متاهل"),
)

SEX_CHOICES = (
    ("0", ""),
    ("1", "مرد"),
    ("2", "زن"),
)

class basic_info(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    military = models.CharField(max_length=50,choices=MILITARY_CHOICES, default='0')
    married = models.CharField(max_length=50,choices=MARRIED_CHOICES, default='0')
    sex = models.CharField(max_length=50,choices=SEX_CHOICES, default='0')
    birth_day = models.CharField(max_length=200, null=True, default='')
    birth_month = models.CharField(max_length=200, null=True, default='')
    birth_year = models.CharField(max_length=200, null=True, default='')
    phone = models.CharField(max_length=200, null=True, default='')
    email = models.CharField(max_length=200, null=True, default='')
    website = models.CharField(max_length=200, null=True, default='')
    summary = models.TextField(null=True, default='')
    user_base_info = models.ForeignKey(User_model, on_delete=models.CASCADE, default='', blank=True, null=True, editable=False)



class user_socialmedia(models.Model):
    social_media = models.CharField(max_length=200)
    username = models.CharField(max_length=200)