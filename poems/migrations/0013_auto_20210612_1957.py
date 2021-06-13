# Generated by Django 3.2.3 on 2021-06-12 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0012_auto_20210612_1935'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AddField(
            model_name='author',
            name='abstract_eo',
            field=models.TextField(default='', verbose_name='abstract'),
        ),
        migrations.AddField(
            model_name='author',
            name='abstract_nl',
            field=models.TextField(default='', verbose_name='abstract'),
        ),
        migrations.AddField(
            model_name='author',
            name='abstract_org',
            field=models.TextField(default='', verbose_name='abstract'),
        ),
    ]