import json

import requests


class NodeRequestException(Exception):
    def __init__(self, status_code, error_message, node_dict):
        self.status_code = status_code
        self.node_dict = node_dict
        super().__init__(error_message)

    def to_dict(self):
        return {
            'url': self.node_dict['url'],
            'status_code': self.status_code,
            'error_message': self.args,
        }


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
            if response.status_code != 200:
                error = 'Unknown error'
                if response.status_code == 400:
                    error = response.json().get('error')
                raise NodeRequestException(response.status_code, error, url_dict)

            last_data = self.filter_by(response.json(), res_fields)

        return last_data
