# Generated by Django 5.1.1 on 2024-10-10 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check_lists', '0002_alter_checklist_options_alter_checklist_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='Название чек-листа'),
        ),
    ]
