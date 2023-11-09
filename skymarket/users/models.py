from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

NULLABLE = {
    'null': True,
    'blank': True
}


class UserRoles(models.TextChoices):
    USER = 'user', _('user')  # Пользователь
    ADMIN = 'admin', _('admin')  # Админ


class CustomUserManager(BaseUserManager):
    """
    Кастомный менеджер пользователей.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
                Создать обычного пользователя.

                Параметры:
                email (str): Email пользователя.
                password (str): Пароль пользователя.
                extra_fields (dict): Дополнительные поля.

                Возвращает:
                User: Созданный пользователь.

                Выбрасывает:
                ValueError: Если email не указан.
                """

        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
                Создать суперпользователя.

                Параметры:
                email (str): Email суперпользователя.
                password (str): Пароль суперпользователя.
                extra_fields (dict): Дополнительные поля.

                Возвращает:
                User: Созданный суперпользователь.

                Выбрасывает:
                ValueError: Если не установлены необходимые атрибуты is_staff и is_superuser.
                """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
        Модель пользователя.

        Атрибуты:
        email (str): Email пользователя.
        first_name (str): Имя пользователя.
        last_name (str): Фамилия пользователя.
        phone (str): Телефон пользователя.
        role (str): Роль пользователя (выбор из UserRoles).
        is_active (bool): Флаг активности пользователя.
        image (ImageField): Аватар пользователя.

        Методы:
        is_admin (property): Возвращает True, если пользователь - администратор.
        is_user (property): Возвращает True, если пользователь - обычный пользователь.
        is_superuser (property): Возвращает True, если пользователь - суперпользователь.
        is_staff (property): Возвращает True, если пользователь - сотрудник.

        has_perm: Проверяет наличие разрешения у пользователя.
        has_module_perms: Проверяет наличие разрешения для модуля.

        __str__: Возвращает email пользователя.
        """

    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    phone = PhoneNumberField('Телефон', unique=True)
    role = models.CharField(max_length=10, choices=UserRoles.choices, default=UserRoles.USER,
                            verbose_name='Роль пользователя')
    is_active = models.BooleanField(verbose_name='Действующий', default=True)
    image = models.ImageField(upload_to='users/avatars', verbose_name='Аватарка', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    objects = CustomUserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
