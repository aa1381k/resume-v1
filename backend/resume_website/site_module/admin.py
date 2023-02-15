from django.contrib import admin
from .models import SiteSetting, SliderModel, FooterLinkBox, FooterLink
# Register your models here.

admin.site.register(SiteSetting)
admin.site.register(SliderModel)
admin.site.register(FooterLinkBox)
admin.site.register(FooterLink)