from dataclasses import dataclass
from typing import List

from domain.model.account_id import AccountId


@dataclass(frozen=True)
class DeleteAccount:
    id: AccountId
