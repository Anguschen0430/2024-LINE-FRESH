# Generated by Django 5.1.3 on 2024-11-19 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='website_url',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='image_url',
            field=models.URLField(default=''),
        ),
    ]
