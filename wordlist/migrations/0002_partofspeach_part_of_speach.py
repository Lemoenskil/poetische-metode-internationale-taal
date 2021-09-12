# Generated by Django 3.2.3 on 2021-09-12 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wordlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partofspeach',
            name='part_of_speach',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parts_of_speech', to='wordlist.acronym'),
        ),
    ]