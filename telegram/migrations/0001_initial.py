# Generated by Django 5.1.1 on 2024-10-10 09:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.PositiveBigIntegerField(unique=True, verbose_name='Телеграм ID')),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='Имя пользователя')),
                ('role', models.CharField(choices=[('user', 'Пользователь'), ('admin', 'Админ')], default='user', max_length=5, verbose_name='Роль пользователя')),
            ],
            options={
                'verbose_name': 'Телеграм пользователь',
                'verbose_name_plural': 'Телеграм пользователи',
            },
        ),
        migrations.CreateModel(
            name='StartQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='Время')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telegram.telegramuser')),
            ],
            options={
                'verbose_name': 'Вопросы о начале работы',
            },
        ),
        migrations.CreateModel(
            name='ReportQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='Время')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telegram.telegramuser')),
            ],
            options={
                'verbose_name': 'Отчёты о работе',
            },
        ),
        migrations.CreateModel(
            name='EndQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='Время')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telegram.telegramuser')),
            ],
            options={
                'verbose_name': 'Вопросы о конце работы',
            },
        ),
    ]