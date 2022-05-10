# Generated by Django 4.0.3 on 2022-05-08 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_resume_data', '0008_user_introduced_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_entartaiment_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('entartaiment_id', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(blank=True, default='', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
