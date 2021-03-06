# Generated by Django 3.2.3 on 2021-07-15 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0022_auto_20210707_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='abstract_en',
            field=models.TextField(default='', verbose_name='abstract'),
        ),
        migrations.AddField(
            model_name='author',
            name='name_en',
            field=models.CharField(default='', max_length=254, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='country',
            name='name_en',
            field=models.CharField(default='', max_length=254, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='genre',
            name='name_en',
            field=models.CharField(default='', max_length=254, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='line',
            name='line_en',
            field=models.CharField(default='', max_length=1024, verbose_name='line'),
        ),
        migrations.AddField(
            model_name='poem',
            name='abstract_en',
            field=models.TextField(default='', verbose_name='abstract'),
        ),
        migrations.AddField(
            model_name='title',
            name='title_en',
            field=models.CharField(default='', max_length=254, verbose_name='title'),
        ),
    ]
