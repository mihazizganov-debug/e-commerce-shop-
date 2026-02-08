from typing import Any, Dict

from src.base_product import BaseProduct
from src.log_mixin import LogMixin


class Product(LogMixin, BaseProduct):
    """
    Класс для представления товара в интернет-магазине.
    Наследуется от BaseProduct и LogMixin.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        # Инициализируем атрибуты
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        # Вызываем миксин (он вызовет BaseProduct.__init__)
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        """Возвращает строку для воссоздания объекта."""
        return f"Product('{self.name}', '{self.description}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать продукты разных типов")
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, product_data: Dict[str, Any]) -> "Product":
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = new_price
