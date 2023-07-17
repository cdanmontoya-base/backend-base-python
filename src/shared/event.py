from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4, UUID


@dataclass
class Event:
    id: UUID
    occurredOn: datetime
    source: str
    name: str
    version: str

    def __init__(self, source: str, version: str) -> None:
        self.id = uuid4()
        self.occurredOn = datetime.now()
        self.name = self.__class__.__name__
        self.source = source
        self.version = version
