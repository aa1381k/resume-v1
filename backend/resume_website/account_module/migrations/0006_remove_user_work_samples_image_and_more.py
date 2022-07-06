# Generated by Django 4.0.3 on 2022-07-04 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0005_alter_user_work_samples_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_work_samples',
            name='image',
        ),
        migrations.AddField(
            model_name='work_samples_image',
            name='image',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='account_module.user_work_samples'),
        ),
    ]
