from django.db import models

# Create your models here.


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200)
    site_url = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, null=True, blank=True)
    fax = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    copy_right = models.TextField()
    about_us_text = models.TextField()
    site_logo = models.ImageField(upload_to='images/site-setting/')
    is_main_setting = models.BooleanField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.site_name


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=500)
    footer_link_box = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class SliderModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url_title = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    slide_image = models.ImageField(default=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title