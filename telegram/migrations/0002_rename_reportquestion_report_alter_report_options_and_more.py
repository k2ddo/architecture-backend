# Generated by Django 5.1.1 on 2024-10-10 12:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReportQuestion',
            new_name='Report',
        ),
        migrations.AlterModelOptions(
            name='report',
            options={'verbose_name': 'Отчёты'},
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('start_question', 'Вопрос о начале дня'), ('report', 'Отчет'), ('end_question', 'Вопрос о конце дня')], max_length=16, verbose_name='Тип напоминания')),
                ('time', models.DateTimeField(verbose_name='Время')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telegram.telegramuser')),
            ],
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.BigIntegerField(verbose_name='ID чата')),
                ('message_id', models.BigIntegerField(verbose_name='ID сообщения')),
                ('text', models.TextField(blank=True, default='', verbose_name='Текст')),
                ('type', models.CharField(choices=[('start_question', 'Вопрос о начале вопрос'), ('report', 'Отчёт'), ('end_question', 'Вопрос о конце дня'), ('other', 'Другое')], max_length=16, verbose_name='Тип вопроса')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telegram.telegramuser')),
            ],
            options={
                'verbose_name': 'Cообщение пользователя',
                'verbose_name_plural': 'Сообщения пользователей',
            },
        ),
        migrations.CreateModel(
            name='UserMessageFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_id', models.CharField(max_length=128, verbose_name='ID файла')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telegram.usermessage')),
            ],
        ),
        migrations.CreateModel(
            name='UserMessageImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_id', models.CharField(max_length=128, verbose_name='ID изображения')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telegram.usermessage')),
            ],
        ),
        migrations.CreateModel(
            name='UserMessageVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_id', models.CharField(max_length=128, verbose_name='ID видео')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telegram.usermessage')),
            ],
        ),
        migrations.CreateModel(
            name='Vacation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telegram.telegramuser')),
            ],
        ),
    ]
