# === Stage 9: Группировка ===
# Project: StarGazer
from collections import Counter


def group_objects_by_type(objects):
    grouped = {}
    for obj in objects:
        obj_type = obj.get("тип")
        if obj_type not in grouped:
            grouped[obj_type] = []
        grouped[obj_type].append(obj)
    return grouped


def count_objects_by_type(objects):
    types = [obj.get("тип") for obj in objects]
    return Counter(types)


def report_counts(counts):
    lines = []
    for obj_type, amount in counts.most_common():
        lines.append(f"{obj_type}: {amount}")
    return "\n".join(lines)


def summarize(objects):
    counts = count_objects_by_type(objects)
    total = sum(counts.values())
    report = report_counts(counts)
    return f"Всего объектов: {total}\n{report}"


if __name__ == "__main__":
    sample = [
        {"название": "Млечный Путь", "тип": "Галактика", "зв_величина": 1.0, "созвездие": "Стрелец"},
        {"название": "Туманность Ориона", "тип": "Туманность", "зв_величина": 4.0, "созвездие": "Орион"},
        {"название": "Плутон", "тип": "Карликовая планета", "зв_величина": 14.0, "созвездие": "Козерог"},
        {"название": "Андромеда", "тип": "Галактика", "зв_величина": 3.4, "созвездие": "Андromеда"},
        {"название": "Сириус", "тип": "Звезда", "зв_величина": -1.46, "созвездие": "Большая Медведица"},
    ]
    print(summarize(sample))
