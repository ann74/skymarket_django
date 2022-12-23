from django.conf import settings
from django.db import models


NULLABLE = {"null": True, "blank": True}


class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тема')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    image = models.ImageField(upload_to='ads', verbose_name='Фото', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ("-created_at",)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    text = models.TextField(verbose_name='Комментарий')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='Объявление')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ("-created_at",)

    def __str__(self):
        return f'{self.text[:15]}...'
