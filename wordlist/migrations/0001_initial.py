# Generated by Django 3.2.3 on 2021-09-12 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acronym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_letter', models.CharField(max_length=1, verbose_name='first_letter')),
            ],
        ),
        migrations.CreateModel(
            name='PartOfSpeach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_eo', models.CharField(default='', max_length=254, verbose_name='name')),
                ('name_nl', models.CharField(default='', max_length=254, verbose_name='name')),
                ('name_org', models.CharField(default='', max_length=254, verbose_name='name')),
                ('name_en', models.CharField(default='', max_length=254, verbose_name='name')),
            ],
            options={
                'verbose_name_plural': 'PartsOfSpeach',
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_eo', models.CharField(default='', max_length=254, verbose_name='word')),
                ('word_nl', models.CharField(default='', max_length=254, verbose_name='word')),
                ('word_org', models.CharField(default='', max_length=254, verbose_name='word')),
                ('word_en', models.CharField(default='', max_length=254, verbose_name='word')),
                ('acronym', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='words', to='wordlist.acronym')),
                ('part_of_speach', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='words', to='wordlist.partofspeach')),
            ],
        ),
    ]
