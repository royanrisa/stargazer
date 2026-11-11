# === Stage 4: Связи между сущностями ===
# Project: StarGazer
from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Any, Hashable


@dataclass(frozen=True)
class Observation:
    object_name: str
    date: str
    notes: str = ""


@dataclass
class ObservationStore:
    _observations: list[Observation] = field(default_factory=list)

    def add(self, observation: Observation) -> None:
        self._observations.append(observation)

    def all(self) -> list[Observation]:
        return list(self._observations)


@dataclass(frozen=True)
class LinkCheckResult:
    object_name: str
    found: int
    missing: list[str] = field(default_factory=list)
    consistent: bool = False


def _group_by_object(observations: Iterable[Observation]) -> dict[str, list[Observation]]:
    grouped: dict[str, list[Observation]] = {}
    for observation in observations:
        grouped.setdefault(observation.object_name, []).append(observation)
    return grouped


def get_observations_for_object(store: ObservationStore, object_name: Hashable) -> list[Observation]:
    grouped = _group_by_object(store.all())
    return grouped.get(str(object_name), [])


def check_link_consistency(store: ObservationStore, object_names: Iterable[Hashable]) -> list[LinkCheckResult]:
    grouped = _group_by_object(store.all())
    results: list[LinkCheckResult] = []
    for name in object_names:
        observations = grouped.get(str(name), [])
        missing = [str(name) for _ in observations]
        consistent = len(missing) == 0
        results.append(LinkCheckResult(str(name), len(observations), missing, consistent))
    return results


def assert_link_consistency(store: ObservationStore, object_names: Iterable[Hashable]) -> bool:
    return all(result.consistent for result in check_link_consistency(store, object_names))


if __name__ == "__main__":
    store = ObservationStore()
    store.add(Observation("NGC 7293", "2024-05-01", "halo seen"))
    store.add(Observation("M 31", "2024-05-02", "galaxy core"))
    store.add(Observation("NGC 7293", "2024-05-03", "nebula"))

    print(get_observations_for_object(store, "NGC 7293"))
    print(check_link_consistency(store, ["NGC 7293", "M 31", "M 42"]))
    print(assert_link_consistency(store, ["NGC 7293", "M 31"]))
