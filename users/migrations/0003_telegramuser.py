# Generated by Django 5.1.1 on 2024-10-10 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_is_approved'),
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
    ]
