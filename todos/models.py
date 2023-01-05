from django.db import models

# Create your models here.


class Todo(models.Model):
    task = models.CharField(max_length=30)
    desc = models.TextField()
    PRIORITIES = (("H", "High",), ("M", "Medium"), ("L", "Low"))
    priority = models.CharField(max_length=1, choices=PRIORITIES, default="L")
    done = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task}"
