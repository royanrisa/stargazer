# === Stage 2: Проверка полей ===
# Project: StarGazer
def normalize_name(name: str) -> str:
    cleaned = name.strip().lower()
    cleaned = " ".join(cleaned.split())
    return cleaned.title()


def normalize_magnitude(value: str) -> float:
    cleaned = value.strip()
    if cleaned in ("", "-", "н/д", "н/д.", "нет", "нет данных"):
        raise ValueError("Звёздную величину нельзя оставить пустой")
    try:
        return float(cleaned)
    except ValueError:
        raise ValueError(
            f"Звёздная величина должна быть числом, получено: {cleaned!r}"
        )


def normalize_constellation(value: str) -> str:
    cleaned = value.strip().lower()
    if cleaned in ("", "-", "н/д", "н/д.", "нет", "нет данных"):
        raise ValueError("Созвездие не может быть пустым")
    cleaned = " ".join(cleaned.split())
    return cleaned.title()


def normalize_type(value: str) -> str:
    cleaned = value.strip().lower()
    if cleaned in ("", "-", "н/д", "н/д.", "нет", "нет данных"):
        raise ValueError("Тип объекта не может быть пустым")
    cleaned = " ".join(cleaned.split())
    return cleaned.title()


def validate_object(
    name: str,
    type_: str,
    magnitude: str,
    constellation: str,
) -> dict:
    normalized = {
        "name": normalize_name(name),
        "type": normalize_type(type_),
        "magnitude": normalize_magnitude(magnitude),
        "constellation": normalize_constellation(constellation),
    }
    if not normalized["name"]:
        raise ValueError("Название объекта не может быть пустым")
    if normalized["name"] in ("объект", "объект наблюдений"):
        raise ValueError(
            "Название не может совпадать с зарезервированным словом «Объект»"
        )
    if normalized["type"] in (
        "тип",
        "тип объекта",
        "тип наблюдательного объекта",
    ):
        raise ValueError(
            "Тип не может совпадать с зарезервированным словом «Тип»"
        )
    if normalized["constellation"] in (
        "созвездие",
        "созвездие объекта",
    ):
        raise ValueError(
            "Созвездие не может совпадать с зарезервированным словом «Созвездие»"
        )
    if normalized["magnitude"] < 0.0:
        raise ValueError(
            "Звёздная величина не может быть отрицательной для этого типа данных"
        )
    return normalized
