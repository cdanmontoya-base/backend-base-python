from abc import ABC, abstractmethod
from typing import List, TypeVar, Optional

T = TypeVar('T')
K = TypeVar('K')


class Repository(ABC):

    @abstractmethod
    def find_by_id(self, k: K) -> Optional[T]:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[T]:
        raise NotImplementedError

    @abstractmethod
    def insert(self, t: T) -> Optional[T]:
        raise NotImplementedError

    @abstractmethod
    def update(self, k: K, data: T):
        raise NotImplementedError

    @abstractmethod
    def delete(self, k: K):
        raise NotImplementedError