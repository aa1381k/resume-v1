from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.basic_info)
admin.site.register(models.user_socialmedia)
admin.site.register(models.user_langurage)
admin.site.register(models.user_skill)
admin.site.register(models.user_certificate_model)
admin.site.register(models.user_education_model)
admin.site.register(models.user_job_model)
