from django.db import models
from django.utils import timezone


class Event(models.Model):

    priorities_list = (
        ('0', 'Sem prioridade'),
        ('1', 'Normal'),
        ('2', 'Urgente'),
        ('3', 'Muito Urgente')
    )

    event = models.CharField(max_length=80)
    date = models.DateField()
    priority = models.CharField(max_length=1, choices=priorities_list)

    def __str__(self):
        return self.event


class Comment(models.Model):
    author = models.CharField(max_length=80)
    email = models.EmailField()
    text = models.CharField(max_length=160)
    date = models.DateTimeField(default=timezone.now)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.author + ' - ' + self.date
