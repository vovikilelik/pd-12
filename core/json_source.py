import json


class JsonSource:

    def __init__(self, default_data=None):
        self.data = default_data

    def load_from_file(self, file_name):
        with open(file_name, encoding='utf-8') as f:
            self.data = json.load(f)

