# === Stage 6: Фильтрация записей ===
# Project: StarGazer
def filter_by_type_and_date(records, target_type, start_date=None, end_date=None):
    """Фильтрует записи объектов по типу и диапазону дат наблюдения.

    records — список словарей с полями:
        name, type, magnitude, constellation, observed_at
    target_type — строка, фильтр по полю type (регистронезависимый поиск).
    start_date / end_date — строки в формате 'YYYY-MM-DD' (необязательно).
    """
    from datetime import datetime

    def parse_date(value):
        if value is None:
            return None
        return datetime.strptime(value, '%Y-%m-%d').date()

    def matches_type(record):
        return record.get('type', '').lower() == target_type.lower()

    def matches_date(record):
        record_date = parse_date(record.get('observed_at'))
        if record_date is None:
            return False
        if start_date is not None and record_date < start_date:
            return False
        if end_date is not None and record_date > end_date:
            return False
        return True

    return [record for record in records if matches_type(record) and matches_date(record)]


def filter_by_type(records, target_type):
    """Удобная обёртка: фильтрация только по типу объекта."""
    return filter_by_type_and_date(records, target_type)


def filter_by_date_range(records, start_date=None, end_date=None):
    """Удобная обёртка: фильтрация только по диапазону дат."""
    return filter_by_type_and_date(records, start_date=start_date, end_date=end_date)
