"""
Тесты для проверки существующей функциональности.
"""

from src.category import Category
from src.product import Product


def test_existing_product_creation():
    """Проверяем, что существующая функциональность Product работает."""
    product = Product("Test", "Test", 100, 5)

    assert product.name == "Test"
    assert product.description == "Test"
    assert product.price == 100
    assert product.quantity == 5


def test_existing_category_creation():
    """Проверяем, что существующая функциональность Category работает."""
    product = Product("Test", "Test", 100, 5)
    category = Category("Test Category", "Test Description", [product])

    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert len(category.products.split("\n")) == 1


def test_product_addition():
    """Проверяем сложение продуктов."""
    product1 = Product("Test1", "Test", 100, 2)
    product2 = Product("Test2", "Test", 200, 3)

    result = product1 + product2
    expected = (100 * 2) + (200 * 3)

    assert result == expected


def test_product_price_setter():
    """Проверяем сеттер цены."""
    product = Product("Test", "Test", 100, 5)

    # Корректная цена
    product.price = 150
    assert product.price == 150

    # Некорректная цена (должно вывести сообщение, но не упасть)
    product.price = -50
    assert product.price == 150  # Цена не изменилась
