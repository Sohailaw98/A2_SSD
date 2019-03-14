from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

class Paste(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField(max_length=524288)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('paste-detail', kwargs={'pk': self.pk})
