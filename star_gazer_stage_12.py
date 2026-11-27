# === Stage 12: История изменений ===
# Project: StarGazer
from datetime import datetime


class ObservationHistory:
    """История изменений для одного объекта наблюдений."""

    def __init__(self, changes=None):
        self.changes = changes if changes is not None else []

    def add_change(self, change, timestamp=None):
        if timestamp is None:
            timestamp = datetime.now()
        self.changes.append(
            {
                "timestamp": timestamp.isoformat(),
                "change": change,
            }
        )

    def get_changes(self):
        return list(self.changes)


def create_default_history():
    history = ObservationHistory()
    history.add_change("Создан объект", datetime.now())
    return history


def log_observation(observation, observation_history):
    observation_history.add_change(
        f"Проведено наблюдение: {observation}", datetime.now()
    )


def update_object_name(name, observation_history):
    observation_history.add_change(f"Изменено название на: {name}", datetime.now())


def get_history_report(observation_history):
    if not observation_history.changes:
        return "История пуста"
    report = "История изменений:\n"
    for change in observation_history.changes:
        report += f"  {change['timestamp']}: {change['change']}\n"
    return report
