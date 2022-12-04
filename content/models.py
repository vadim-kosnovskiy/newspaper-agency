from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from newspaper import settings


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("content:redactor-detail", kwargs={"pk": self.pk})


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    publishers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="newspapers")

    def __str__(self):
        return self.title


class Article(models.Model):
    article_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True, blank=True)
    published_date = models.DateField(null=True, blank=True)
    hyper_reference = models.CharField(max_length=255, null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)
    newspaper = models.ForeignKey(Newspaper, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ["article_title"]

    def __str__(self):
        return f"{self.article_title}"
