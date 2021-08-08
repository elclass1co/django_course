# Generated by Django 3.1.7 on 2021-08-04 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20210804_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.CharField(blank=True, max_length=150, verbose_name='тэги')),
                ('about_me', models.TextField(blank=True, verbose_name='о себе')),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'М'), ('FEMALE', 'Ж')], max_length=6, verbose_name='пол')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
