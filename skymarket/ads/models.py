from datetime import datetime

from django.db import models

from users.models import User, NULLABLE


class Ad(models.Model):
    """Модель Объявления"""

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True)
    price = models.PositiveIntegerField()
    author = models.ForeignKey(User, related_name="ads", on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="ads/img", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Модель Комментария"""

    text = models.TextField(max_length=1000)
    author = models.ForeignKey(User, related_name="comments", on_delete=models.SET_NULL, null=True)
    ad = models.ForeignKey(Ad, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['-created_at']

    def __str__(self):
        text = str(self.text)
        return text if len(text) <= 20 else text[:20] + "..."