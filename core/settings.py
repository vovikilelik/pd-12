from core.json_source import JsonSource


class Settings(JsonSource):

    def get(self, name, default_value=None):
        if name in self.data:
            return self.data[name]
        else:
            return default_value
