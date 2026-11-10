# === Stage 3: Хранилище в памяти ===
# Project: StarGazer
import uuid


class ObservationObject:
    def __init__(self, name, object_type, magnitude, constellation):
        self.id = uuid.uuid4()
        self.name = name
        self.type = object_type
        self.magnitude = magnitude
        self.constellation = constellation

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "type": self.type,
            "magnitude": self.magnitude,
            "constellation": self.constellation,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            object_type=data["type"],
            magnitude=data["magnitude"],
            constellation=data["constellation"],
        )

    def __repr__(self):
        return (
            f"ObservationObject(id={self.id}, name={self.name!r}, "
            f"type={self.type!r}, magnitude={self.magnitude}, "
            f"constellation={self.constellation!r})"
        )


class ObjectStore:
    def __init__(self):
        self._objects = {}

    def add(self, name, object_type, magnitude, constellation):
        obj = ObservationObject(name, object_type, magnitude, constellation)
        self._objects[obj.id] = obj
        return obj

    def add_from_dict(self, data):
        obj = ObservationObject.from_dict(data)
        self._objects[obj.id] = obj
        return obj

    def get(self, object_id):
        return self._objects.get(object_id)

    def list(self):
        return list(self._objects.values())

    def __len__(self):
        return len(self._objects)
