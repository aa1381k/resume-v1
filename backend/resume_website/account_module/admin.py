from django.contrib import admin
from .models import User_model, user_work_samples, work_samples_image
# Register your models here.

admin.site.register(User_model)
admin.site.register(user_work_samples)
admin.site.register(work_samples_image)