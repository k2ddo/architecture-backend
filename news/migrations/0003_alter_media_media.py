# Generated by Django 5.0.7 on 2024-08-01 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_options_alter_media_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='media',
            field=models.FileField(upload_to='', verbose_name='Медиа'),
        ),
    ]