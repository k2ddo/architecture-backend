from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Кастомная модель пользователя"""
    is_approved = models.BooleanField('Одобрить пользователя', default=False)


class Task(models.Model):
    """Модель задач для пользователя"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    title = models.CharField(max_length=64, verbose_name='Заголовок')
    description = models.TextField('Описание')
    duration = models.CharField(max_length=16, verbose_name='Длительность')
    due_date = models.DateField('Дата реализации')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
