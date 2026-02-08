from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseProduct(ABC):
    """Абстрактный базовый класс для товаров."""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: Any) -> float:
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: Dict[str, Any]) -> "BaseProduct":
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        pass
