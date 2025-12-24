from django.db import models

from config.settings import NULLABLE
from users.models import User

class Point(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=250, verbose_name='Описание')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Широта')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Долгота')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    delete_at = models.DateTimeField(auto_now_add=False, verbose_name='Дата и время удаления', **NULLABLE, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Точка"
        verbose_name_plural = "Точки"

class Message(models.Model):
    point = models.ForeignKey(Point, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField(max_length=250, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"



