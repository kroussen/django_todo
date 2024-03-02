from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название задачи')
    description = models.TextField(verbose_name='Описание задачи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания задачи')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования задачи')
    due_date = models.DateField(blank=True, null=True, verbose_name='Дата завершения задачи')
    completed = models.BooleanField(default=False, verbose_name='Завершена?')

    PRIORITY_CHOICES = [
        ('низкий', 'Низкий'),
        ('средний', 'Средний'),
        ('высокий', 'Высокий'),
    ]

    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES, default='средний', verbose_name='Приоритет')

    def __str__(self):
        return f"{self.title}: {self.completed}"
