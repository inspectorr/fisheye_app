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
