from dataclasses import dataclass
from uuid import UUID


@dataclass()
class AccountId:
    id: UUID
