from abc import ABC, abstractmethod
from pydantic import BaseModel


class Base(BaseModel, ABC):

    @abstractmethod
    def from_dict(data: dict):
        pass