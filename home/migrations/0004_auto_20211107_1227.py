# Generated by Django 3.2.3 on 2021-11-07 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20211107_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='learn_a_new_language_en',
            field=models.TextField(blank=True, default='', verbose_name='learn_a_new_language'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='learn_a_new_language_eo',
            field=models.TextField(blank=True, default='', verbose_name='learn_a_new_language'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='learn_a_new_language_nl',
            field=models.TextField(blank=True, default='', verbose_name='learn_a_new_language'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='learn_a_new_language_org',
            field=models.TextField(blank=True, default='', verbose_name='learn_a_new_language'),
        ),
    ]
