# === Stage 11: Статусы записей ===
# Project: StarGazer
import datetime

OBJECT_LIFECYCLE_STATES = (
    "discovered",
    "cataloged",
    "observed",
    "archived",
)

LIFECYCLE_TRANSITIONS = {
    "discovered": {"cataloged"},
    "cataloged": {"observed"},
    "observed": {"archived"},
    "archived": set(),
}


class ObjectLifecycleError(ValueError):
    def __init__(self, source_state, target_state):
        self.source_state = source_state
        self.target_state = target_state
        allowed = LIFECYCLE_TRANSITIONS.get(source_state, frozenset())
        allowed_states = ", ".join(sorted(allowed)) or "<нет допустимых>"
        message = (
            f"Недопустимый переход объекта из состояния "
            f"'{source_state}' в состояние '{target_state}'. "
            f"Допустимые переходы из '{source_state}': {allowed_states}."
        )
        super().__init__(message)
