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

    def test_product_zero_quantity(self) -> None:
        """Тест создания продукта с нулевым количеством."""
        product = Product("Товар", "Описание", 100.0, 0)

        assert product.quantity == 0
        assert isinstance(product.quantity, int)

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

    # ДЗ 14.2 - новые тесты ниже

    def test_price_getter(self) -> None:
        """Тест геттера для цены (ДЗ 14.2)."""
        product = Product("Телефон", "Смартфон", 10000.0, 10)
        # Проверяем что геттер работает
        assert product.price == 10000.0
        # Проверяем что атрибут приватный
        assert hasattr(product, "_price")

    def test_price_setter_positive(self) -> None:
        """Тест сеттера для положительной цены (ДЗ 14.2)."""
        product = Product("Телефон", "Смартфон", 10000.0, 10)
        product.price = 15000.0
        assert product.price == 15000.0
        assert product._price == 15000.0

    def test_price_setter_negative(self, capsys) -> None:
        """Тест сеттера для отрицательной цены (ДЗ 14.2)."""
        product = Product("Телефон", "Смартфон", 10000.0, 10)
        product.price = -5000.0
        captured = capsys.readouterr()
        # Цена не должна измениться
        assert product.price == 10000.0
        # Должно вывестись сообщение
        assert "Цена не должна быть нулевая или отрицательная" in captured.out

    def test_price_setter_zero(self, capsys) -> None:
        """Тест сеттера для нулевой цены (ДЗ 14.2)."""
        product = Product("Телефон", "Смартфон", 10000.0, 10)
        product.price = 0
        captured = capsys.readouterr()
        # Цена не должна измениться
        assert product.price == 10000.0
        # Должно вывестись сообщение
        assert "Цена не должна быть нулевая или отрицательная" in captured.out

    def test_new_product_classmethod(self) -> None:
        """Тест класс-метода new_product (ДЗ 14.2)."""
        product_data = {
            "name": "Ноутбук",
            "description": "Игровой ноутбук",
            "price": 150000.0,
            "quantity": 3,
        }
        product = Product.new_product(product_data)

        assert product.name == "Ноутбук"
        assert product.description == "Игровой ноутбук"
        assert product.price == 150000.0
        assert product.quantity == 3
        # Проверяем что создан правильный тип объекта
        assert isinstance(product, Product)

    # ДЗ 15.1 - новые тесты ниже

    def test_product_str_method(self) -> None:
        """Тест метода __str__ для Product."""
        product = Product("Телефон", "Смартфон", 10000.0, 10)
        expected = "Телефон, 10000.0 руб. Остаток: 10 шт."
        assert str(product) == expected

    def test_product_add_method(self) -> None:
        """Тест метода __add__ для Product."""
        product1 = Product("Товар1", "Описание1", 100.0, 5)
        product2 = Product("Товар2", "Описание2", 200.0, 3)

        result = product1 + product2
        assert result == 1100.0

        # Проверяем что складываются правильно в обе стороны
        result2 = product2 + product1
        assert result2 == 1100.0

    def test_product_add_with_wrong_type(self) -> None:
        """Тест, что нельзя сложить Product с не-Product."""
        product = Product("Товар", "Описание", 100.0, 5)

        with pytest.raises(TypeError, match="Можно складывать только объекты Product"):
            _ = product + 100  # type: ignore

        with pytest.raises(TypeError):
            _ = product + "строка"  # type: ignore
