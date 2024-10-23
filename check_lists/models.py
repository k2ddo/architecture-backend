from django.db import models
from django.core.validators import FileExtensionValidator

class CheckList(models.Model):
    """Модель чек-листов"""
    CHECK_LISTS_TYPES = (
        ('check_list', 'Чек-лист'),
        ('estimate', 'Смета'),
    )

    name = models.CharField(max_length=64,
                            verbose_name='Название чек-листа',
                            null=False,
                            unique=True)

    type = models.CharField(max_length=10,
                            verbose_name='Тип чек-листа',
                            choices=CHECK_LISTS_TYPES,
                            default='check_list')

    file = models.FileField('Файл .xlsx',
                            upload_to='',
                            null=False,
                            validators=[FileExtensionValidator(['xlsx'])])

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Чек-лист'
        verbose_name_plural = 'Чек-листы'

