# === Stage 5: Генерация идентификаторов ===
# Project: StarGazer
import string
import secrets


PROJECT_PREFIX = "SG"


def _is_valid_slug(name):
    cleaned = "".join(c for c in name if c.isalnum() or c == " ")
    cleaned = cleaned.strip().lower()
    cleaned = "".join(c if c.isalnum() else "-" for c in cleaned)
    cleaned = cleaned.strip("-")
    return bool(cleaned)


def generate_id(prefix, used_ids, counter=0):
    alphabet = string.ascii_lowercase
    while True:
        random_part = "".join(secrets.choice(alphabet) for _ in range(6))
        candidate = f"{prefix}-{counter}-{random_part}"
        if candidate not in used_ids:
            used_ids.add(candidate)
            return candidate
        counter += 1


class IdentifierRegistry:

    def __init__(self, prefix=PROJECT_PREFIX):
        self.prefix = prefix
        self._used = set()
        self._counter = 0

    def is_available(self, candidate=None):
        if candidate is None:
            return True
        return candidate not in self._used

    def reserve(self, value):
        if not self.is_available(value):
            raise ValueError(f"Идентификатор '{value}' уже существует")
        self._used.add(value)
        return value

    def allocate(self, length=6):
        alphabet = string.ascii_lowercase
        self._counter += 1
        random_part = "".join(secrets.choice(alphabet) for _ in range(length))
        candidate = f"{self.prefix}-{self._counter}-{random_part}"
        while not self.is_available(candidate):
            self._counter += 1
            random_part = "".join(secrets.choice(alphabet) for _ in range(length))
            candidate = f"{self.prefix}-{self._counter}-{random_part}"
        self._used.add(candidate)
        return candidate

    def clear(self):
        self._used.clear()
        self._counter = 0

    def get_used(self):
        return set(self._used)
