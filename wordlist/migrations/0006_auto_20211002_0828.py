# Generated by Django 3.2.3 on 2021-10-02 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wordlist', '0005_auto_20211002_0752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wordgroup',
            name='misc_en',
        ),
        migrations.RemoveField(
            model_name='wordgroup',
            name='misc_eo',
        ),
        migrations.RemoveField(
            model_name='wordgroup',
            name='misc_nl',
        ),
        migrations.RemoveField(
            model_name='wordgroup',
            name='misc_org',
        ),
        migrations.RemoveField(
            model_name='wordgroup',
            name='noun_en',
        ),
        migrations.RemoveField(
            model_name='wordgroup',
            name='noun_eo',
        ),
        migrations.RemoveField(
            model_name='wordgroup',
            name='noun_nl',
        ),
        migrations.RemoveField(
            model_name='wordgroup',
            name='noun_org',
        ),
        migrations.RemoveField(
            model_name='wordgroup',
            name='verb_en',
        ),
        migrations.RemoveField(
            model_name='wordgroup',
            name='verb_eo',
        ),
        migrations.RemoveField(
            model_name='wordgroup',
            name='verb_nl',
        ),
        migrations.RemoveField(
            model_name='wordgroup',
            name='verb_org',
        ),
        migrations.CreateModel(
            name='Verb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verb_eo', models.CharField(blank=True, default='', max_length=254, verbose_name='word')),
                ('verb_nl', models.CharField(blank=True, default='', max_length=254, verbose_name='word')),
                ('verb_org', models.CharField(blank=True, default='', max_length=254, verbose_name='word')),
                ('verb_en', models.CharField(blank=True, default='', max_length=254, verbose_name='word')),
                ('word_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='verb', to='wordlist.wordgroup')),
            ],
        ),
        migrations.CreateModel(
            name='Noun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noun_eo', models.CharField(blank=True, default='', max_length=254, verbose_name='word')),
                ('noun_nl', models.CharField(blank=True, default='', max_length=254, verbose_name='word')),
                ('noun_org', models.CharField(blank=True, default='', max_length=254, verbose_name='word')),
                ('noun_en', models.CharField(blank=True, default='', max_length=254, verbose_name='word')),
                ('word_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noun', to='wordlist.wordgroup')),
            ],
        ),
        migrations.CreateModel(
            name='Misc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('misc_eo', models.CharField(blank=True, default='', max_length=254, verbose_name='word')),
                ('misc_nl', models.CharField(blank=True, default='', max_length=254, verbose_name='word')),
                ('misc_org', models.CharField(blank=True, default='', max_length=254, verbose_name='word')),
                ('misc_en', models.CharField(blank=True, default='', max_length=254, verbose_name='word')),
                ('word_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='misc', to='wordlist.wordgroup')),
            ],
        ),
    ]
