from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)  # Title of the task
    description = models.TextField(blank=True)  # Optional description
    completed = models.BooleanField(default=False)  # Task completion status
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the task is created

    def __str__(self):
        return self.title
