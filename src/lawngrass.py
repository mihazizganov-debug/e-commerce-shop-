"""Модуль с классом LawnGrass."""

from src.product import Product


class LawnGrass(Product):
    """
    Класс для представления травы газонной.
    Наследуется от класса Product и добавляет специфичные для травы газонной атрибуты.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Инициализирует новый экземпляр класса LawnGrass."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        """Строковое представление травы газонной."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self) -> str:
        """Формальное строковое представление травы газонной."""
        return (
            f"LawnGrass('{self.name}', '{self.description}', {self.price}, "
            f"{self.quantity}, '{self.country}', '{self.germination_period}', "
            f"'{self.color}')"
        )
