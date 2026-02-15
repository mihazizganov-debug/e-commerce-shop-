import pytest

from src.product import Product


def test_product_creation():
    """Тест создания продукта с корректными данными."""
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 50000.0
    assert product.quantity == 10


def test_product_creation_with_zero_quantity():
    """Тест создания продукта с нулевым количеством."""
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_new_product_with_zero_quantity():
    """Тест создания продукта через метод new_product с нулевым количеством."""
    product_data = {
        "name": "Бракованный товар",
        "description": "Неверное количество",
        "price": 1000.0,
        "quantity": 0,
    }

    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product.new_product(product_data)


def test_price_setter_negative(capsys):
    """Тест установки отрицательной цены."""
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 50000.0  # Цена не должна измениться


def test_price_setter_zero(capsys):
    """Тест установки нулевой цены."""
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 50000.0  # Цена не должна измениться


def test_price_setter_positive():
    """Тест установки положительной цены."""
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    product.price = 45000.0
    assert product.price == 45000.0


def test_product_str():
    """Тест строкового представления продукта."""
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    assert str(product) == "Телефон, 50000.0 руб. Остаток: 10 шт."


def test_product_repr():
    """Тест repr представления продукта."""
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    expected = "Product('Телефон', 'Смартфон', 50000.0, 10)"
    assert repr(product) == expected


def test_product_addition():
    """Тест сложения продуктов."""
    product1 = Product("Товар 1", "Описание 1", 100.0, 5)
    product2 = Product("Товар 2", "Описание 2", 200.0, 3)

    result = product1 + product2
    expected = (100.0 * 5) + (200.0 * 3)  # 500 + 600 = 1100
    assert result == expected


def test_product_addition_different_types():
    """Тест сложения продуктов разных типов."""

    class Smartphone(Product):
        pass

    product1 = Product("Товар 1", "Описание 1", 100.0, 5)
    product2 = Smartphone("Товар 2", "Описание 2", 200.0, 3)

    with pytest.raises(TypeError, match="Нельзя складывать продукты разных типов"):
        product1 + product2
