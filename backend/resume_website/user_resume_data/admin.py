from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.basic_info_model)
admin.site.register(models.user_socialmedia_model)
admin.site.register(models.user_langurage_model)
admin.site.register(models.user_skill_model)
admin.site.register(models.user_certificate_model)
admin.site.register(models.user_education_model)
admin.site.register(models.user_job_model)
admin.site.register(models.user_projects_model)
admin.site.register(models.user_internship_model)
admin.site.register(models.user_introduced_model)
admin.site.register(models.user_entertainment_model)
