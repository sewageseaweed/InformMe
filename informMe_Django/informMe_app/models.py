from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    # tags = models.TextChoices("Natural Disaster", "Human Rights")
    links = models.TextField()
    # image = models.FilePathField(path="/img")