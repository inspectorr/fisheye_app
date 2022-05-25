from django.db import models


class Node(models.Model):
    url = models.URLField(unique=True)
    name = models.TextField(unique=True)
    description = models.TextField(blank=True, null=True)
