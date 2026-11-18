# === Stage 7: Поиск по нескольким словам ===
# Project: StarGazer
def parse_query(query):
    """Разбор строки поиска на ключевые слова и исключения.

    Ключевые слова — не пустые куски, не начинающиеся с «-».
    Исключения — куски, начинающиеся с «-» (причём знак «-» входит
    в сам элемент и не участвует в совпадении).
    """
    tokens = query.split()
    keywords = []
    exclusions = set()
    for token in tokens:
        if token.startswith("-"):
            exclusions.add(token[1:].lower())
        elif token:
            keywords.append(token.lower())
    return keywords, exclusions


def tokens_match(text, keywords, exclusions):
    """Правда, если текст содержит все ключевые слова и ни одно исключение."""
    text = text.lower()
    if any(word in exclusions for word in exclusions):
        return False
    return all(word in text for word in keywords)


def find_objects(objects, query):
    """Поиск объектов по нескольким словам с поддержкой исключений.

    objects — список объектов, каждый объект должен предоставлять строку
    для сравнения через метод get_search_text().
    """
    keywords, exclusions = parse_query(query)
    if not keywords:
        return list(objects)
    return [obj for obj in objects if tokens_match(obj.get_search_text(), keywords, exclusions)]


def get_search_text(obj):
    """Стандартное представление объекта для текстового поиска."""
    return "{title} {type} {constellation}".format(
        title=obj.title,
        type=obj.type,
        constellation=obj.constellation,
    )


if __name__ == "__main__":
    class Object:
        def __init__(self, title, type_, constellation):
            self.title = title
            self.type = type_
            self.constellation = constellation
            self._search = None

        def get_search_text(self):
            if self._search is None:
                self._search = get_search_text(self)
            return self._search

    data = [
        Object("M42", "Туманность", "Орион"),
        Object("NGC 2244", "Звёздное скопление", "Орион"),
        Object("M45", "Звёздное скопление", "Орион"),
        Object("M13", "Глобулярное скопление", "Геркулес"),
    ]

    print(find_objects(data, "орион"))
    print(find_objects(data, "геркулес"))
    print(find_objects(data, "скопление -глобулярное"))
    print(find_objects(data, "tumbanost"))
