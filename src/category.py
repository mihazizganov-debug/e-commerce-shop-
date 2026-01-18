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

    def add_product(self, product: Product) -> None:
        """Добавление товара в категорию."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для получения строкового представления товаров."""
        products_info = []
        for product in self.__products:
            products_info.append(
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            )
        return "\n".join(products_info)
