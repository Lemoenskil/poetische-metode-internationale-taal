# Generated by Django 3.2.3 on 2021-10-31 08:34

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VoiceRecording',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_eo', models.CharField(default='', max_length=254, verbose_name='name')),
                ('title_nl', models.CharField(default='', max_length=254, verbose_name='name')),
                ('title_org', models.CharField(default='', max_length=254, verbose_name='name')),
                ('title_en', models.CharField(default='', max_length=254, verbose_name='name')),
                ('audio_file', filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audio_file', to='filer.file')),
            ],
        ),
    ]