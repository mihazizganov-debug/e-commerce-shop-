"""Дополнительные тесты для класса Category."""

import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


class TestCategoryEnhanced:
    """Класс для тестирования расширенной функциональности Category."""

    def test_add_product_valid_types(self):
        """Тест добавления продуктов разных валидных типов."""
        category = Category("Электроника", "Техника", [])

        # Базовый продукт
        product = Product("Ноутбук", "Игровой ноутбук", 1500, 3)
        category.add_product(product)
        assert category.category_count > 0

        # Смартфон
        smartphone = Smartphone("iPhone", "Смартфон", 1000, 5, 3.0, "15", 256, "Black")
        category.add_product(smartphone)

        # Трава газонная
        grass = LawnGrass("Трава", "Газонная", 50, 100, "Россия", "14 дней", "Зеленая")
        category.add_product(grass)

    def test_add_product_invalid_type(self):
        """Тест добавления невалидного типа объекта."""
        category = Category("Тест", "Тестовая категория", [])

        # Попытка добавить строку
        with pytest.raises(
            TypeError, match="Можно добавлять только продукты и их наследников"
        ):
            category.add_product("Не продукт")

        # Попытка добавить число
        with pytest.raises(
            TypeError, match="Можно добавлять только продукты и их наследников"
        ):
            category.add_product(123)

        # Попытка добавить список
        with pytest.raises(
            TypeError, match="Можно добавлять только продукты и их наследников"
        ):
            category.add_product([1, 2, 3])

    def test_product_addition_restriction_in_category(self):
        """Тест, что в категории можно хранить разные типы продуктов."""
        category = Category("Разное", "Разные товары", [])

        product = Product("Книга", "Интересная книга", 20, 10)
        smartphone = Smartphone("Телефон", "Смартфон", 500, 3, 2.5, "A1", 64, "Silver")
        grass = LawnGrass("Трава", "Для газона", 30, 50, "USA", "10 дней", "Green")

        category.add_product(product)
        category.add_product(smartphone)
        category.add_product(grass)

        assert category.product_count > 0
