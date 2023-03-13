from django.urls import reverse
from django.db import models
from datetime import date


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    created = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article:article-detail", kwargs={"id": self.id})
