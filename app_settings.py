from core.settings import Settings


class AppSettings(Settings):

    @property
    def online(self):
        return self.get('online', False)

    @property
    def case_sensitive(self):
        return self.get('case-sensitive', False)

    @property
    def limit(self):
        return self.get('limit', 1)
