from django.db import models

# Create your models here.
class TodoItem(models.Model):
    content = models.TextField()
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.content