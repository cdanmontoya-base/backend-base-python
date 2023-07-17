from dataclasses import dataclass

from domain.model.account_id import AccountId
from domain.model.contact_information import ContactInformation


@dataclass()
class Account:
    id: AccountId
    contact_information: ContactInformation
