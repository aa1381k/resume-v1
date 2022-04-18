# Generated by Django 4.0.3 on 2022-04-18 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_resume_data', '0005_alter_basic_info_birth_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic_info',
            name='birth_month',
            field=models.CharField(choices=[('0', ''), ('1', 'فروردین'), ('2', 'اردیبهشت'), ('3', 'خرداد'), ('4', 'تیر'), ('5', 'مرداد'), ('6', 'شهریور'), ('7', 'مهر'), ('8', 'آبان'), ('9', 'آذر'), ('10', 'دی'), ('11', 'بهمن'), ('12', 'اسفند')], default='', max_length=200, null=True),
        ),
    ]
