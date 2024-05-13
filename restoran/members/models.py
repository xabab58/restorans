from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(
        verbose_name='Табельный номер',
        max_length=150,
        unique=True,
        help_text='Обязательное. Только цифры, без i.',
        error_messages={
            'unique': "Пользователь с таким именем уже существует.",
        },
    )
    patronymic = models.CharField(max_length=50, blank=True, null=True, verbose_name="Отчество")


