"""
Модуль с классом Smartphone.
"""

from src.product import Product


class Smartphone(Product):
    """
    Класс для представления смартфона.
    Наследуется от класса Product.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """
        Инициализирует новый экземпляр класса Smartphone.
        """
        # Сначала устанавливаем специфичные атрибуты
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        # Затем вызываем родительский __init__
        super().__init__(name, description, price, quantity)

    def __str__(self) -> str:
        """Строковое представление смартфона."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self) -> str:
        """Формальное строковое представление смартфона."""
        return (
            f"Smartphone('{self.name}', '{self.description}', {self.price}, "
            f"{self.quantity}, {self.efficiency}, '{self.model}', "
            f"{self.memory}, '{self.color}')"
        )
