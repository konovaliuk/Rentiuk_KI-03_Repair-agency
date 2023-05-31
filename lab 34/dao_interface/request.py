from abc import ABC, abstractmethod
from model.models import Request


class RequestIDAO(ABC):
    @abstractmethod
    def select(self, request_id: int):
        pass

    @abstractmethod
    def insert(self, request: Request):
        pass

    @abstractmethod
    def update(self, request: Request):
        pass

    @abstractmethod
    def delete(self, request_id: int):
        pass