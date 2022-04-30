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

DAY_CHOICES = (
    ("0", ""),("1", "1"),
    ("2", "2"),("3", "3"),
    ("4", "4"),("5", "5"),
    ("6", "6"),("7", "7"),
    ("8", "8"),("9", "9"),
    ("10", "10"),("11", "11"),
    ("12", "12"),("13", "13"),
    ("14", "14"),("15", "15"),
    ("16", "16"),("17", "17"),
    ("18", "18"),("19", "19"),
    ("20", "20"),("21", "21"),
    ("22", "22"),("23", "23"),
    ("24", "24"),("25", "25"),
    ("26", "26"),("27", "27"),
    ("28", "28"),("29", "29"),
    ("30", "30"),("31", "31"),
)

MONTH_CHOICES = (
    ("0", ""),
    ("1", "فروردین"),
    ("2", "اردیبهشت"),
    ("3", "خرداد"),
    ("4", "تیر"),
    ("5", "مرداد"),
    ("6", "شهریور"),
    ("7", "مهر"),
    ("8", "آبان"),
    ("9", "آذر"),
    ("10", "دی"),
    ("11", "بهمن"),
    ("12", "اسفند"),
)

class basic_info(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    job_title = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    military = models.CharField(max_length=50,choices=MILITARY_CHOICES, default='0')
    married = models.CharField(max_length=50,choices=MARRIED_CHOICES, default='0')
    sex = models.CharField(max_length=50,choices=SEX_CHOICES, default='0')
    birth_day = models.CharField(max_length=200, choices=DAY_CHOICES, null=True, default='')
    birth_month = models.CharField(max_length=200, choices=MONTH_CHOICES, null=True, default='')
    birth_year = models.CharField(max_length=200, null=True, default='')
    phone = models.CharField(max_length=200, null=True, default='')
    email = models.CharField(max_length=200, null=True, default='')
    website = models.CharField(max_length=200, null=True, default='')
    summary = models.TextField(null=True, default='')
    avatar = models.ImageField(upload_to='images/user-profile',default='')
    resume_id = models.CharField(max_length=200, null=True, default='')
    is_active = models.BooleanField(default=False)
    user_base_info = models.ForeignKey(User_model, on_delete=models.CASCADE, default='', blank=True, null=True, editable=False)
    social_media = models.ForeignKey("user_socialmedia", on_delete=models.CASCADE, default='', blank=True, null=True, editable=False)
    # langurage = models.ForeignKey("user_langurage", on_delete=models.CASCADE, default='', blank=True, null=True, editable=False)

    def __str__(self):
        return self.first_name + " " + self.last_name



class user_socialmedia(models.Model):
    social_media = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    social_id = models.CharField(max_length=200, null=True, default='')
    user = models.ForeignKey(User_model, on_delete=models.CASCADE, default='', blank=True, null=True, editable=False)


    def __str__(self):
        return self.social_media


class user_langurage(models.Model):
    langurage = models.CharField(max_length=200)
    grade = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    lang_id = models.CharField(max_length=200, null=True, default='')
    user = models.ForeignKey(User_model, on_delete=models.CASCADE, default='', blank=True, null=True, editable=False)

    def __str__(self):
        return self.langurage

class user_skill(models.Model):
    skill = models.CharField(max_length=200, null=True, blank=True)
    grade = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    skill_id = models.CharField(max_length=200, null=True, default='')
    user = models.ForeignKey(User_model, on_delete=models.CASCADE, default='', blank=True, null=True, editable=False)

    def __str__(self):
        return self.skill


class user_certificate_model(models.Model):
    certificate_title = models.CharField(max_length=200, null=True, blank=True)
    organization_title = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.CharField(max_length=200, null=True, blank=True)
    end_date = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    certificate_id = models.CharField(max_length=200, null=True, default='')
    user = models.ForeignKey(User_model, on_delete=models.CASCADE, default='', blank=True, null=True, editable=False)

    def __str__(self):
        return self.certificate_title


class user_education_model(models.Model):
    education_title = models.CharField(max_length=200, null=True, blank=True)
    education_grade = models.CharField(max_length=200, null=True, blank=True)
    university_name = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.CharField(max_length=200, null=True, blank=True)
    end_date = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(default='', null=True, blank=True)
    education_id = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User_model, on_delete=models.CASCADE, default='', blank=True, null=True, editable=False)

    def __str__(self):
        return self.education_title

class user_job_model(models.Model):
    job_title = models.CharField(max_length=200, null=True, blank=True)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.CharField(max_length=200, null=True, blank=True)
    end_date = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(default='', null=True, blank=True)
    job_id = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User_model, on_delete=models.CASCADE, default='', blank=True, null=True, editable=False)

    def __str__(self):
        return self.job_title
