# === Stage 8: Теги ===
# Project: StarGazer
"""StarGazer: Этап 8 — теги для «объект».

Модуль самодостаточный: свои классы и функции, только стандартная
библиотека. Работает с экземплярами объектов, предположительно
заведёнными в предыдущих этапах проекта.
"""

from typing import Iterable, List, Optional


__all__ = ["Tag", "TagManager", "tags_for_object", "add_tag", "remove_tag",
            "find_by_tag", "object_has_tag"]


class Tag:
    """Простой тег, привязанный к астрономическому объекту."""

    __slots__ = ("name", "object_name")

    def __init__(self, name: str, object_name: str) -> None:
        self.name = name
        self.object_name = object_name

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tag):
            return NotImplemented
        return self.name == other.name and self.object_name == other.object_name

    def __hash__(self) -> int:
        return hash((self.name, self.object_name))

    def __repr__(self) -> str:
        return f"Tag({self.object_name!r}, {self.name!r})"


class TagManager:
    """Управляет тегами для одного или нескольких объектов.

    Тег создаётся автоматически при добавлении. Хранит теги в
    словаре «название тега» -> «название объекта», чтобы исключить
    дубликаты одного и того же тега для разных объектов.
    """

    def __init__(self) -> None:
        self._tags: dict[str, str] = {}

    def add_tag(self, object_name: str, tag_name: str) -> Tag:
        """Добавить тег к объекту. Возвращает созданный экземпляр Tag.

        Если тег уже существует для этого объекта — ничего не меняется.
        """
        key = (tag_name, object_name)
        if key in self._tags:
            return Tag(tag_name, object_name)

        tag = Tag(tag_name, object_name)
        self._tags[key] = object_name
        return tag

    def remove_tag(self, object_name: str, tag_name: str) -> bool:
        """Удалить тег от объекта. Возвращает True, если тег был удалён."""
        return self._tags.pop((tag_name, object_name), None) is not None

    def find_by_tag(self, tag_name: str) -> List[str]:
        """Найти все объекты, имеющие указанный тег. Возвращает список."""
        return [object_name for (t, object_name) in self._tags
                if t == tag_name]

    def object_has_tag(self, object_name: str, tag_name: str) -> bool:
        """Проверить, имеет ли объект указанный тег."""
        return (tag_name, object_name) in self._tags

    def tags_for_object(self, object_name: str) -> List[str]:
        """Вернуть список названий всех тегов для указанного объекта."""
        return [t for (t, o) in self._tags if o == object_name]

    def all_tags(self) -> Iterable[str]:
        """Вернуть все уникальные названия тегов."""
        return tuple(self._tags.keys())


def tags_for_object(object_name: str, manager: TagManager) -> List[str]:
    return manager.tags_for_object(object_name)


def add_tag(object_name: str, tag_name: str, manager: TagManager) -> Tag:
    return manager.add_tag(object_name, tag_name)


def remove_tag(object_name: str, tag_name: str, manager: TagManager) -> bool:
    return manager.remove_tag(object_name, tag_name)


def find_by_tag(tag_name: str, manager: TagManager) -> List[str]:
    return manager.find_by_tag(tag_name)


def object_has_tag(object_name: str, tag_name: str, manager: TagManager) -> bool:
    return manager.object_has_tag(object_name, tag_name)
