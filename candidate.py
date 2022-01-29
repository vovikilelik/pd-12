class Candidate:

    def __init__(self, record):
        self._record = record

    @property
    def id(self):
        return self._record['id']

    @property
    def name(self):
        return self._record['name']

    @property
    def picture(self):
        return self._record['picture']

    @property
    def gender(self):
        return self._record['gender']

    @property
    def age(self):
        return self._record['age']

    @property
    def skills(self):
        return self._record['skills']

    def map(self):
        return self._record

    def __str__(self):
        return f'{self._record}'
