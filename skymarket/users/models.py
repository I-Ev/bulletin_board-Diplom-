from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон', **NULLABLE)
    role = models.CharField(choices=[
        ('user', 'User'),
        ('admin', 'Admin'),
    ], max_length=10, default='user', verbose_name='Роль')
    image = models.ImageField(upload_to='users/avatars', verbose_name='Аватарка', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
