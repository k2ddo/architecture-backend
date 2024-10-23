from django.db import models


class TelegramUser(models.Model):
    """Телеграм модель пользователя для бота по задачам"""
    telegram_id = models.PositiveBigIntegerField('Телеграм ID',
                                                 unique=True)

    username = models.CharField(max_length=32,
                                verbose_name='Имя пользователя',
                                unique=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Телеграм пользователь'
        verbose_name_plural = 'Телеграм пользователи'


class Vacation(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, related_name='vacation')
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

    def __str__(self):
        return f'{self.user} ({self.start_date} - {self.end_date})'

    class Meta:
        verbose_name = 'Отпуск'
        verbose_name_plural = 'Отпуска'


class Notification(models.Model):
    TYPES = (
        ('start', 'Начало работы'),
        ('report', 'Отчёт'),
        ('end', 'Завершение работы'),
    )

    user = models.ForeignKey(TelegramUser,
                             on_delete=models.CASCADE,
                             related_name='notifications')
    type = models.CharField(max_length=12,
                            verbose_name='Тип',
                            choices=TYPES,
                            default='start')
    time = models.TimeField('Время', null=False)

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name = 'Уведомления'


class Reminder(models.Model):
    TYPES = (
        ('start_question', 'Вопрос о начале дня'),
        ('report', 'Отчет'),
        ('end_question', 'Вопрос о конце дня'),
    )

    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    type = models.CharField(max_length=16,
                            verbose_name='Тип напоминания',
                            choices=TYPES,
                            null=False)
    time = models.DateTimeField('Время', null=False)

    def __str__(self) -> None:
        return f'{self.user} - {self.get_type_display()}'

    class Meta:
        verbose_name = 'Напоминание'
        verbose_name_plural = 'Напоминания'


class UserMessage(models.Model):
    TYPES = (
        ('start_question', 'Вопрос о начале дня'),
        ('report', 'Отчёт'),
        ('end_question', 'Вопрос о конце дня'),
        ('other', 'Другое'),
    )

    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, null=False)
    chat_id = models.BigIntegerField('ID чата', null=False)
    message_id = models.BigIntegerField('ID сообщения', null=False)
    text = models.TextField(verbose_name='Текст', blank=True, default='')
    type = models.CharField(max_length=16,
                            verbose_name='Тип вопроса',
                            choices=TYPES,
                            null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text} -> {self.created_at}'

    class Meta:
        verbose_name = 'Cообщение пользователя'
        verbose_name_plural = 'Сообщения пользователей'


class UserMessageImage(models.Model):
    message = models.ForeignKey(UserMessage, on_delete=models.CASCADE)
    file_id = models.CharField(max_length=128, verbose_name='ID изображения')


class UserMessageVideo(models.Model):
    message = models.ForeignKey(UserMessage, on_delete=models.CASCADE)
    file_id = models.CharField(max_length=128, verbose_name='ID видео')

class UserMessageFile(models.Model):
    message = models.ForeignKey(UserMessage, on_delete=models.CASCADE)
    file_id = models.CharField(max_length=128, verbose_name='ID файла')
