# Generated by Django 4.0.3 on 2022-04-18 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_resume_data', '0008_alter_basic_info_resume_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_socialmedia',
            name='social_id',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
