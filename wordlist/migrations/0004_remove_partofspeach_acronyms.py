# Generated by Django 3.2.3 on 2021-09-12 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordlist', '0003_rename_part_of_speach_partofspeach_acronyms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partofspeach',
            name='acronyms',
        ),
    ]
