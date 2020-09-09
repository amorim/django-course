from django.db import models
from django.utils import timezone


class Event(models.Model):
    event = models.CharField(max_length=80)
    date = models.DateTimeField()
    priorities_list = (
        ('0', 'Sem prioridade'),
        ('1', 'Normal'),
        ('2', 'Urgente'),
        ('3', 'Muito Urgente')
    )
    priority = models.CharField(max_length=1, choices=priorities_list)

    def __str__(self):
        return self.event

    @property
    def text_priority(self):
        for k, v in self.priorities_list:
            if k == self.priority:
                return v
        return ''


class Comment(models.Model):
    author = models.CharField(max_length=80)
    email = models.EmailField()
    text = models.CharField(max_length=160)
    date = models.DateTimeField(default=timezone.now)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comment_event')

    def __str__(self):
        return "{} comentou em {:%c}".format(self.author, self.date)

    class Meta:
        ordering = ('-date',)