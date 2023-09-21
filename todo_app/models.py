from django.db import models


# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Task: {self.title}"

