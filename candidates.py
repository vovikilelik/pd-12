from candidate import Candidate
from core.database import Database, element_comparator


def skill_comparator(record, **args):
    """
    Функция сравнения по полю навыков
    """
    skill = args['skill'].lower()
    source_skills = [s for s in record['skills'].split(',') if skill == s.lower()]

    return len(source_skills) > 0


def get_text_comparator(case_sensitive=False):
    """
    Возвращает функцию сравнения по вхождению подстроки для неопределённого поля
    """

    def text_equals(source, value):
        source_text = str(source) if case_sensitive else str(source).lower()
        value_text = str(value) if case_sensitive else str(value).lower()

        return source_text.find(value_text) > -1

    def comparator(record, **args):
        return element_comparator(record, is_equals=text_equals, **args)

    return comparator


class Candidates(Database):

    def get_by_id(self, candidate_id):
        """
        Возвращает элемент по уникальному идентификатору
        """
        record = self.search_record(id=candidate_id)

        if record is not None:
            return Candidate(record)

    def search_by_skill(self, skill, limit=None):
        """
        Возвращает список элементов, где найден хотя бы один навык
        """
        records = self.search_records(comparator=skill_comparator, limit=limit, skill=skill)

        return [Candidate(record) for record in records]

    def search_by_text(self, case_sensitive=False, **args):
        """
        Возвращает список элементов, где есть все вхождения подстроки во всех переданных аргументах
        """
        comparator = get_text_comparator(case_sensitive=case_sensitive)
        records = self.search_records(comparator=comparator, **args)

        return [Candidate(record) for record in records]
