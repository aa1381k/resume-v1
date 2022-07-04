# Generated by Django 4.0.3 on 2022-07-02 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0002_alter_user_model_bg_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_work_samples',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('post_link', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('post_description', models.TextField()),
                ('post_id', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(blank=True, default='', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='work_samples_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_image', models.FileField(upload_to='images/work-samples/')),
                ('post_id', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('image', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='account_module.user_work_samples')),
                ('user', models.ForeignKey(blank=True, default='', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
