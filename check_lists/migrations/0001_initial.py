# Generated by Django 5.1.1 on 2024-10-04 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название чек-листа')),
                ('type', models.CharField(choices=[('check_list', 'Чек-лист'), ('estimate', 'Смета')], max_length=10, verbose_name='Тип чек-листа')),
                ('file', models.FileField(upload_to='', verbose_name='Файл .xlsx')),
            ],
        ),
    ]
