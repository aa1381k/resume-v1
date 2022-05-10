from django.db import models

# Create your models here.


class contact_us_model(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    text = models.TextField(default='')

    def __str__(self):
        return self.subject