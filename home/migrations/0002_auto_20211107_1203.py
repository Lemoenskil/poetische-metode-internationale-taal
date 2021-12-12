# Generated by Django 3.2.3 on 2021-11-07 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='about_en',
            field=models.TextField(blank=True, default='', verbose_name='about'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='about_eo',
            field=models.TextField(blank=True, default='', verbose_name='about'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='about_nl',
            field=models.TextField(blank=True, default='', verbose_name='about'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='about_org',
            field=models.TextField(blank=True, default='', verbose_name='about'),
        ),
    ]