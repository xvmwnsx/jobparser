from django.conf import settings
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    
    position = models.CharField(
        max_length=255,
        verbose_name='Должность'
    )
    
    location = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Регион'
    )
    
    salary = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Зарплата'
    )

    skills = models.TextField(
        blank=True,
        verbose_name='Навыки'
    )

    notify_by_email = models.BooleanField(
        default=True,
        verbose_name='Email-уведомления'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'

    
class Resume(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='resume'
    )

    file = models.FileField(
        upload_to='resumes/',
        verbose_name='Файл резюме'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    parsed = models.BooleanField(
        default=False,
        verbose_name='Резюме обработано'
    )

    def __str__(self):
        return f'Резюме пользователя {self.user.username}'