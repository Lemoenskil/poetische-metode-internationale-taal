# Generated by Django 3.2.3 on 2021-07-07 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0020_poem_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='country_of_birth',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='poems.country'),
        ),
    ]
