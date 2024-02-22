from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field


class Articles(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DR", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=250)
    summery = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = CKEditor5Field("Text", config_name='extends')
    author = models.ForeignKey(get_user_model(), models.CASCADE, related_name='articles_author')
    photo = models.ImageField(upload_to="images/", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(timezone.now())
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-published"]
        indexes = [
            models.Index(fields=["-published"])
        ]

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])


class Comments(models.Model):
    article = models.ForeignKey(Articles, models.CASCADE, related_name="comments")
    comment = models.TextField()
    author = models.ForeignKey(get_user_model(), models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


