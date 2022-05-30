import json
import logging
import os

import requests
from django.apps import apps
from django.core.exceptions import ValidationError
from django.utils import timezone

from nodes.exceptions import NodeRequestException


class UrlListRunner:
    def __init__(self, serialized_urls):
        self.urls = serialized_urls

    @staticmethod
    def filter_by(data, fields_set):
        filtered = {}
        for name in fields_set:
            if name in data:
                filtered[name] = data[name]
        return filtered

    def run(self, initial_data=None):
        last_data = initial_data.copy() or {}

        for url_dict in self.urls:
            url = url_dict['url']
            req_fields = url_dict['req_fields']
            res_fields = url_dict['res_fields']
            default_json_params = url_dict['default_json_params']

            data = default_json_params.copy()
            data.update(last_data)

            payload = self.filter_by(data, req_fields)
            response = requests.post(url=url, data=json.dumps(payload), headers={'content-type': 'application/json'})
            json_data = {}
            try:
                json_data = response.json()
            except Exception as e:
                logging.exception(e)
            if response.status_code != 200:
                error = 'Unknown error'
                if response.status_code == 400:
                    error = json_data.get('error', 'No error parsed from json data')
                raise NodeRequestException(response.status_code, error, url_dict)

            last_data = self.filter_by(json_data, res_fields)

        return last_data


def validate_uploading_image(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.png', '.jpg', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported image extension, please upload .png or .jp(e)g')


class FilterBenchmarkRunner:
    def __init__(self, filter_id, request_json=dict):
        self.filter_id = filter_id
        self.start = timezone.now()
        self.request_json = request_json

    def end(self, response_json=dict):
        FilterBenchmark = apps.get_model('nodes', 'FilterBenchmark')
        delta = timezone.now() - self.start
        benchmark = FilterBenchmark.objects.create(
            filter_id=self.filter_id,
            ms=delta.seconds * 1e6 + delta.microseconds,
            request_json=self.request_json,
            response_json=response_json,
        )
        return benchmark
