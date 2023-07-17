from dataclasses import dataclass
from typing import List


@dataclass()
class ContactInformation:
    email: str
    cellphones: List[str]
