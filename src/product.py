"""Модуль с классом Product."""

from typing import Any, Dict


class Product:
    """Класс для представления товара в интернет-магазине."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализирует новый экземпляр класса Product."""
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Строковое представление товара."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """
        Сложение двух товаров одного типа.
        Возвращает сумму произведений цены на количество для каждого товара.
        """
        if type(self) != type(other):  # noqa: E721
            raise TypeError("Нельзя складывать продукты разных типов")

        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, product_data: Dict[str, Any]) -> "Product":
        """Класс-метод для создания нового товара из словаря."""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self) -> float:
        """Геттер для цены товара."""
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены товара с проверкой."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = new_price
