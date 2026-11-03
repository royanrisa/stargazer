# === Stage 1: Каркас модуля ===
# Project: StarGazer
from dataclasses import dataclass


@dataclass
class SkyObject:
    name: str
    object_type: str
    apparent_magnitude: float
    constellation: str


def create_demo_objects() -> list[SkyObject]:
    return [
        SkyObject("Сириус", "Звезда", -1.46, "Близнецов"),
        SkyObject("Вега", "Звезда", 0.03, "Лев"),
        SkyObject("М42", "Туманность", 4.0, "Орион"),
        SkyObject("NGC 7293", "Галактика", 4.0, "Лира"),
        SkyObject("Плутон", "Карликовая планета", 14.0, "Козерог"),
    ]


def main() -> None:
    print("StarGazer — журнал астрономических наблюдений")
    print("=" * 40)
    for obj in create_demo_objects():
        print(f"{obj.name:<12} | {obj.object_type:<16} | "
              f"m={obj.apparent_magnitude:>5.2f} | {obj.constellation}")


if __name__ == "__main__":
    main()
