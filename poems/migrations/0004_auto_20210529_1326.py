# Generated by Django 3.2.3 on 2021-05-29 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0003_auto_20210529_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='line_org',
            field=models.CharField(default='', max_length=1024, verbose_name='line'),
        ),
        migrations.AddField(
            model_name='title',
            name='title_org',
            field=models.CharField(default='', max_length=254, verbose_name='title'),
        ),
    ]
