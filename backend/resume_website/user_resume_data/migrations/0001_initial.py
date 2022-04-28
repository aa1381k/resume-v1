# Generated by Django 4.0.3 on 2022-04-28 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='user_socialmedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_media', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('social_id', models.CharField(default='', max_length=200, null=True)),
                ('user', models.ForeignKey(blank=True, default='', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user_skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=200)),
                ('grade', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('skill_id', models.CharField(default='', max_length=200, null=True)),
                ('user', models.ForeignKey(blank=True, default='', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user_langurage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('langurage', models.CharField(max_length=200)),
                ('grade', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('lang_id', models.CharField(default='', max_length=200, null=True)),
                ('user', models.ForeignKey(blank=True, default='', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user_certificate_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_title', models.CharField(max_length=200)),
                ('organization_title', models.CharField(max_length=200)),
                ('start_date', models.CharField(max_length=200)),
                ('end_date', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('certificate_id', models.CharField(default='', max_length=200, null=True)),
                ('user', models.ForeignKey(blank=True, default='', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='basic_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('military', models.CharField(choices=[('0', ''), ('1', 'مشمول'), ('2', 'در حال خدمت'), ('3', 'پایان خدمت'), ('4', 'معاف'), ('5', 'معافیت تحصیلی'), ('6', 'معافیت پزشکی'), ('7', 'معافیت غیر پزشکی')], default='0', max_length=50)),
                ('married', models.CharField(choices=[('0', ''), ('1', 'مجرد'), ('2', 'متاهل')], default='0', max_length=50)),
                ('sex', models.CharField(choices=[('0', ''), ('1', 'مرد'), ('2', 'زن')], default='0', max_length=50)),
                ('birth_day', models.CharField(choices=[('0', ''), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31')], default='', max_length=200, null=True)),
                ('birth_month', models.CharField(choices=[('0', ''), ('1', 'فروردین'), ('2', 'اردیبهشت'), ('3', 'خرداد'), ('4', 'تیر'), ('5', 'مرداد'), ('6', 'شهریور'), ('7', 'مهر'), ('8', 'آبان'), ('9', 'آذر'), ('10', 'دی'), ('11', 'بهمن'), ('12', 'اسفند')], default='', max_length=200, null=True)),
                ('birth_year', models.CharField(default='', max_length=200, null=True)),
                ('phone', models.CharField(default='', max_length=200, null=True)),
                ('email', models.CharField(default='', max_length=200, null=True)),
                ('website', models.CharField(default='', max_length=200, null=True)),
                ('summary', models.TextField(default='', null=True)),
                ('avatar', models.ImageField(default='', upload_to='images/user-profile')),
                ('resume_id', models.CharField(default='', max_length=200, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('social_media', models.ForeignKey(blank=True, default='', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_resume_data.user_socialmedia')),
                ('user_base_info', models.ForeignKey(blank=True, default='', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
