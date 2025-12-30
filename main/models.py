from django.db import models
from django.conf import settings
USER = settings.AUTH_USER_MODEL

class StatusChoices(models.TextChoices):
    TODO = 'todo', 'todo'
    IN_PROGRESS = 'inprogress', 'inprogress'
    COMPLETED = 'completed', 'completed'

class Plan(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=15, choices=StatusChoices.choices)

    user = models.ForeignKey(USER, on_delete=models.CASCADE)

    def __str__(self):
        return self.title