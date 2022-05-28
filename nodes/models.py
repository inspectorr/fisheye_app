from urllib.parse import urljoin

from django.db import models

from nodes.constants import DEFAULT_REQ_FIELDS, DEFAULT_RES_FIELDS


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
        ).order_by('index')

    def __str__(self):
        return self.name


class FilterNode(models.Model):
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE, related_name='filter_nodes')
    node = models.ForeignKey(Node, on_delete=models.PROTECT)
    index = models.PositiveIntegerField()
    default_json_params = models.JSONField(default=dict, null=True, blank=True)

    def __str__(self):
        return f'Node of 🐟"{self.filter.name}"🐟: 👁"{self.node.name}"👁 ({self.index + 1})'

    class Meta:
        unique_together = ('filter', 'index')
