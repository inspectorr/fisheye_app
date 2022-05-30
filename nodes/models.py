from urllib.parse import urljoin

from django.db import models
from django.utils import timezone

from application import settings
from nodes.constants import DEFAULT_REQ_FIELDS, DEFAULT_RES_FIELDS
from nodes.helpers import validate_uploading_image


class Microservice(models.Model):
    url = models.URLField(unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.url


class Node(models.Model):
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255, unique=True)
    microservice = models.ForeignKey(Microservice, on_delete=models.SET_NULL, blank=True, null=True)
    req_fields = models.TextField(help_text=f"""
    allowed comma-separated request json data field names, example:
    {DEFAULT_REQ_FIELDS}
    """, default=DEFAULT_REQ_FIELDS)
    res_fields = models.TextField(help_text=f"""
    allowed comma-separated response json data field names, example:
    {DEFAULT_RES_FIELDS}
    """, default=DEFAULT_RES_FIELDS)
    description = models.TextField(blank=True, null=True)

    def get_full_url(self):
        """
        node: do not forget to:
        .select_related(
            'node',
            'node__microservice'
        )
        when using this from qs to optimize
        """
        if self.microservice:
            return urljoin(self.microservice.url, self.url)
        return self.url

    def __str__(self):
        return self.name


class Filter(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def get_ordered_filter_nodes(self):
        return self.filter_nodes.all().select_related(
            'node',
            'node__microservice'
        ).exclude(enabled=False).order_by('index')

    def get_last_benchmark(self):
        return self.benchmarks.all().last()

    def __str__(self):
        return self.name


class FilterNode(models.Model):
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE, related_name='filter_nodes')
    node = models.ForeignKey(Node, on_delete=models.PROTECT)
    index = models.PositiveIntegerField()
    default_json_params = models.JSONField(default=dict, null=True, blank=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return f'Node of 🐟"{self.filter.name}"🐟: 👁"{self.node.name}"👁 ({self.index + 1})'

    class Meta:
        unique_together = ('filter', 'index')


class StaticImage(models.Model):
    image = models.ImageField(upload_to='static/', validators=[validate_uploading_image])

    def get_url(self):
        return self.image.url

    def get_full_url(self):
        return urljoin(settings.SITE_URL, self.get_url())

    def __str__(self):
        return self.get_full_url()


class FilterBenchmark(models.Model):
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE, related_name='benchmarks')
    ms = models.PositiveBigIntegerField()
    request_json = models.JSONField(default=dict)
    response_json = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.filter.name + ' ' + str(self.created_at)

    @staticmethod
    def start():
        return timezone.now()
