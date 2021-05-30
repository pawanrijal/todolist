from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200)
    task_time=models.DateField(auto_now_add=True)
    completed=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title