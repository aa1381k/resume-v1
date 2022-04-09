from django.db import models

# Create your models here.
from django.utils.text import slugify


class Slider(models.Model):
    template_image = models.ImageField(upload_to='images/slider-images',verbose_name="عکس اسلاید")
    template_name = models.CharField(max_length=200, verbose_name="اسم اسلاید", blank=False, null=False)
    slug = models.SlugField(default='',null=False, db_index=True, blank=True, unique=True, editable=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.template_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.template_name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'عکس اسلایدر'
        verbose_name_plural = 'عکس های اسلایدر'


class home_page_settings(models.Model):
    title = models.CharField(max_length=200, default='')
    show_counter = models.BooleanField(verbose_name="نمایش تعداد رزومه ها")
    home_page_image = models.ImageField(upload_to="images/home-page")
    is_active = models.BooleanField(default='')



class about_us_model(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/about-us')
    text = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
