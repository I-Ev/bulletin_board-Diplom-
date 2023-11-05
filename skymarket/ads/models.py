from datetime import datetime

from django.db import models

from users.models import User, NULLABLE


class Ad(models.Model):
    """
       Модель для хранения информации об объявлениях.

       Поля:
       - title (CharField): Заголовок объявления, максимум 200 символов.
       - description (TextField): Описание объявления, максимум 1000 символов (необязательное поле).
       - price (PositiveIntegerField): Цена объявления.
       - author (ForeignKey): Связь с моделью User для указания автора объявления (может быть null).
       - image (ImageField): Изображение объявления (может быть null).
       - created_at (DateTimeField): Дата и время создания объявления (автоматически заполняется).

       Метаданные:
       - verbose_name: Название модели в единственном числе.
       - verbose_name_plural: Название модели во множественном числе.
       - ordering: Сортировка объявлений по умолчанию - по дате создания в обратном порядке.

       Методы:
       - __str__: Возвращает строковое представление объекта, используется для отображения в административной панели.

       """


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
    """
        Модель для хранения комментариев к объявлениям.

        Поля:
        - text (TextField): Текст комментария, максимум 1000 символов.
        - author (ForeignKey): Связь с моделью User для указания автора комментария (может быть null).
        - ad (ForeignKey): Связь с моделью Ad для указания объявления, к которому относится комментарий.
        - created_at (DateTimeField): Дата и время создания комментария (автоматически заполняется).

        Метаданные:
        - verbose_name: Название модели в единственном числе.
        - verbose_name_plural: Название модели во множественном числе.
        - ordering: Сортировка комментариев по умолчанию - по дате создания в обратном порядке.

        Методы:
        - __str__: Возвращает строковое представление объекта, используется для отображения в административной панели.

        """

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
