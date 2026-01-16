import pytest

from src.product import Product


class TestProduct:
    """Тестирование функциональности класса Product."""

    def test_product_initialization(self) -> None:
        """Тест инициализации продукта с обычными значениями."""
        product = Product("Телефон", "Смартфон", 10000.0, 10)

        assert product.name == "Телефон"
        assert product.description == "Смартфон"
        assert product.price == 10000.0
        assert product.quantity == 10

    def test_product_with_decimal_price(self) -> None:
        """Тест создания продукта с дробной ценой."""
        product = Product("Книга", "Художественная", 999.99, 5)

        assert product.price == 999.99
        assert isinstance(product.price, float)

    def test_product_zero_quantity(self) -> None:
        """Тест создания продукта с нулевым количеством."""
        product = Product("Товар", "Описание", 100.0, 0)

        assert product.quantity == 0
        assert isinstance(product.quantity, int)

    def test_product_large_quantity(self) -> None:
        """Тест создания продукта с большим количеством."""
        product = Product("Сахар", "Килограмм", 50.0, 1000)

        assert product.quantity == 1000

    def test_product_negative_price_raises_no_error(self) -> None:
        """Тест: продукт с отрицательной ценой создается без ошибки."""
        product = Product("Товар", "Описание", -100.0, 5)

        assert product.price == -100.0

    def test_product_attributes_types(self) -> None:
        """Тест типов данных атрибутов продукта."""
        product = Product("Ноутбук", "Игровой", 50000.0, 3)

        assert isinstance(product.name, str)
        assert isinstance(product.description, str)
        assert isinstance(product.price, float)
        assert isinstance(product.quantity, int)

    def test_product_string_representation(self) -> None:
        """Тест строкового представления объекта Product."""
        product = Product("Тест", "Описание", 100.0, 5)

        # Проверяем, что объект имеет строковое представление
        repr_str = repr(product)
        assert "Product" in repr_str
        assert "Тест" in repr_str or "object at" in repr_str

    def test_product_equality_by_reference(self) -> None:
        """Тест сравнения продуктов по ссылке."""
        product1 = Product("Товар", "Описание", 100.0, 5)
        product2 = Product("Товар", "Описание", 100.0, 5)
        product3 = product1  # Та же ссылка

        assert product1 is not product2  # Разные объекты
        assert product1 is product3  # Один и тот же объект

    def test_product_modify_attributes(self) -> None:
        """Тест изменения атрибутов продукта после создания."""
        product = Product("Исходный", "Описание", 100.0, 5)

        # Меняем атрибуты
        product.name = "Измененный"
        product.price = 200.0
        product.quantity = 10

        assert product.name == "Измененный"
        assert product.price == 200.0
        assert product.quantity == 10

    def test_product_with_special_characters(self) -> None:
        """Тест создания продукта со спецсимволами в названии."""
        product = Product("Товар №1", "Описание с 'кавычками'", 100.0, 5)

        assert product.name == "Товар №1"
        assert "кавычками" in product.description
