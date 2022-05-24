from django.db import models


class Node(models.Model):
    url = models.URLField()
    description = models.TextField()
