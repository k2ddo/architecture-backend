from django.db import models


class News(models.Model):
    """Основная модель новостей"""
    title = models.CharField(max_length=100, verbose_name='Заголовок', null=False)
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self) -> str:
        return self.title
	
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Media(models.Model):
    """Модель медиа контента новостей"""
    MEDIA_TYPES = (
        ('image', 'Изображение'),
        ('video', 'Видео'),
        ('file', 'Файл'),
    )

    news = models.ForeignKey(News, on_delete=models.CASCADE, null=False, related_name='media')
    media = models.FileField('Медиа', upload_to='', null=False)
    media_type = models.CharField(max_length=10,
                                  choices=MEDIA_TYPES,
                                  default='file',
                                  verbose_name='Тип медиа')

    def __str__(self) -> str:
        return f"{self.media_type}: {self.media.name}"


class Url(models.Model):
    """Модель ссылки новостей"""
    title = models.CharField(max_length=100, verbose_name='Текст ссылки')
    url = models.URLField(verbose_name='URL')
    news = models.ForeignKey(News, on_delete=models.CASCADE, null=True, related_name='urls')

    def __str__(self) -> str:
        return self.title

