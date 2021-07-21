from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=500)
    auth = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.pk)])
