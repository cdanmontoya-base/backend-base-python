from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class InsertAccount:
    email: str
    cellphones: List[str]
