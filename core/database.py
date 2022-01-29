from core.json_source import JsonSource


def strict_equals(source, search):
    return source == search


def element_comparator(record, is_equals=strict_equals, **args):
    """
    Функция сравнения элементов
    :param record: входящий элемент
    :param is_equals: функция сравнения по полю
    :param args: список аргументов для сравнения
    :return: boolean
    """
    for key, value in args.items():
        if key not in record or not is_equals(record[key], value):
            return False

    return True


class Database(JsonSource):

    def search_records(self, comparator=element_comparator, limit=None, **args):
        result = []

        for record in self.data:
            if limit is not None and limit <= len(result):
                break

            if comparator(record, **args):
                result.append(record)

        return result

    def search_record(self, comparator=element_comparator, **args):
        records = self.search_records(comparator=comparator, limit=1, **args)
        return records[0] if len(records) > 0 else None
