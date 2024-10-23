# Generated by Django 5.1.1 on 2024-10-16 10:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0004_remove_telegramuser_role_alter_endquestion_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='user',
        ),
        migrations.RemoveField(
            model_name='startquestion',
            name='user',
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('start', 'Начало работы'), ('report', 'Отчёт'), ('end', 'Завершение работы')], default='start', max_length=12, verbose_name='Тип')),
                ('time', models.TimeField(verbose_name='Время')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='telegram.telegramuser')),
            ],
            options={
                'verbose_name': 'Уведомления',
            },
        ),
        migrations.DeleteModel(
            name='EndQuestion',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
        migrations.DeleteModel(
            name='StartQuestion',
        ),
    ]