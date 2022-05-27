from urllib.parse import urljoin

from django.db import models


class Microservice(models.Model):
    url = models.URLField(unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.url


class Node(models.Model):
    url = models.URLField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    microservice = models.ForeignKey(Microservice, on_delete=models.SET_NULL, blank=True, null=True)

    @property
    def base_url(self):
        if self.microservice:
            return urljoin(self.microservice.url, self.url)
        return self.url


class Filter(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # todo iterator


class FilterNode(models.Model):
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE)
    node_value = models.ForeignKey(Node, on_delete=models.CASCADE)
    next_filter_node = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
