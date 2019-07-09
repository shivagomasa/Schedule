from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=70)
    date = models.DateField(blank=True,null=True)
    time = models.TimeField(blank=True,null=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail',args=[str(self.id)])