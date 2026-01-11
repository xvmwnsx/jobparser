from django.db import models
from django.contrib.postgres.fields import ArrayField

class Vacancy(models.Model):
    source = models.CharField(max_length=50, verbose_name="Источник")
    external_id = models.CharField(max_length=100, verbose_name="ID вакансии в источнике")
    source_url = models.URLField(verbose_name="URL вакансии")
    title = models.CharField(max_length=255, verbose_name="Название")
    company = models.CharField(max_length=255, blank=True, verbose_name="Компания")
    description = models.TextField(blank=True, verbose_name="Описание")
    location = models.CharField(max_length=255, blank=True, verbose_name="Локация")
    required_skills = ArrayField(
        models.CharField(max_length=100), 
        default=list, 
        blank=True, 
        verbose_name="Навыки"
        )
    experience_min = models.PositiveIntegerField(default=0, verbose_name="Опыт от")
    salary_min = models.PositiveIntegerField(null=True, blank=True)
    salary_max = models.PositiveIntegerField(null=True, blank=True)
    employment_type = models.CharField(max_length=50, blank=True, verbose_name="Тип занятости")
    remote = models.BooleanField(default=False, verbose_name="Удаленно")
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        constraints = [
            models.UniqueConstraint(
                fields=["source", "external_id"],
                name="unique_vacancy_per_source"
            )
        ]
        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["experience_min"]),
            models.Index(fields=["source"]),
            models.Index(fields=["is_active"]),

        ]

    def __str__(self):
        return self.title
