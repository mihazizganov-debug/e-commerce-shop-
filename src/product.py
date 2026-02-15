from typing import Any, Dict

from src.base_product import BaseProduct
from src.log_mixin import LogMixin


class Product(LogMixin, BaseProduct):
    """
    Класс для представления товара в интернет-магазине.
    Наследуется от BaseProduct и LogMixin.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализирует новый экземпляр класса Product.

        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара
            quantity: Количество товара

        Raises:
            ValueError: Если количество товара равно 0
        """
        # Проверка на нулевое количество
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

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
        """
        Создает новый продукт из словаря с данными.

        Args:
            product_data: Словарь с данными продукта

        Returns:
            Product: Новый экземпляр продукта

        Raises:
            ValueError: Если количество товара равно 0
        """
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
