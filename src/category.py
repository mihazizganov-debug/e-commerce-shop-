"""Модуль с классом Category."""

from typing import List

from src.product import Product


class Category:
    """Класс для представления категории товаров в интернет-магазине."""

    # Атрибуты класса
    category_count = 0  # Общее количество категорий
    product_count = 0  # Общее количество товаров

    def __init__(self, name: str, description: str, products: List[Product]):
        """Инициализирует новый экземпляр класса Category."""
        self.name = name
        self.description = description
        self.__products = products

        # Увеличиваем счетчики
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """Добавление товара в категорию."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только продукты и их наследников")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для получения строкового представления товаров."""
        return "\n".join(str(product) for product in self.__products)

    @property
    def products_list(self) -> List[Product]:
        """Геттер для получения списка товаров."""
        return self.__products

    def middle_price(self) -> float:
        """
        Подсчитывает средний ценник всех товаров в категории.

        Returns:
            float: Средняя цена товаров или 0, если в категории нет товаров
        """
        try:
            # Суммируем цены всех товаров и делим на их количество
            total_sum = sum(product.price for product in self.__products)
            return total_sum / len(self.__products)
        except ZeroDivisionError:
            # Если в категории нет товаров, возвращаем 0
            return 0.0
