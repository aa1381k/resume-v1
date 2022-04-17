# Generated by Django 4.0.3 on 2022-04-17 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_resume_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic_info',
            name='user_base_info',
            field=models.ForeignKey(blank=True, default='', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
