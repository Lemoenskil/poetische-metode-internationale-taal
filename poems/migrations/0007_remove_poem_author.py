# Generated by Django 3.2.3 on 2021-06-12 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0006_auto_20210612_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poem',
            name='author',
        ),
    ]