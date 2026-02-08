"""
Тесты для миксина LogMixin.
"""

import pytest

from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_log_mixin_prints_on_creation(capsys):
    """При создании объекта должна печататься информация."""
    Product("Test Product", "Test Description", 100.5, 10)

    captured = capsys.readouterr()
    assert "Создан объект класса" in captured.out
    assert "Product('Test Product'" in captured.out
    assert "100.5" in captured.out
    assert "10" in captured.out


def test_log_mixin_with_smartphone(capsys):
    """Миксин должен работать с Smartphone."""
    Smartphone(
        name="iPhone",
        description="Test",
        price=1000,
        quantity=5,
        efficiency=95.5,
        model="15 Pro",
        memory=256,
        color="Black",
    )

    captured = capsys.readouterr()
    assert "Создан объект класса" in captured.out
    assert "Smartphone(" in captured.out
    assert "'iPhone'" in captured.out
    assert "1000" in captured.out
    assert "5" in captured.out


def test_log_mixin_with_lawn_grass(capsys):
    """Миксин должен работать с LawnGrass."""
    LawnGrass(
        name="Трава",
        description="Test",
        price=100,
        quantity=50,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )

    captured = capsys.readouterr()
    assert "Создан объект класса" in captured.out
    assert "LawnGrass(" in captured.out
    assert "'Трава'" in captured.out
    assert "100" in captured.out
    assert "50" in captured.out


def test_repr_method():
    """Проверяем метод __repr__."""
    product = Product("Test Product", "Test Description", 100.5, 10)
    repr_str = repr(product)

    assert repr_str.startswith("Product(")
    assert "'Test Product'" in repr_str
    assert "100.5" in repr_str
    assert "10" in repr_str


def test_existing_functionality():
    """Проверяем, что старая функциональность работает."""
    product = Product("Test", "Test", 100, 5)

    assert product.name == "Test"
    assert product.description == "Test"
    assert product.price == 100
    assert product.quantity == 5

    product2 = Product("Test2", "Test", 200, 3)
    result = product + product2
    assert result == (100 * 5) + (200 * 3)


def test_log_mixin_shows_class_and_basic_params():
    """Проверяем, что LogMixin показывает класс и базовые параметры."""
    import sys
    from io import StringIO

    captured_output = StringIO()
    sys.stdout = captured_output

    Product("Laptop", "Gaming laptop", 1500.0, 3)

    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

    assert "Создан объект класса Product(" in output
    assert "'Laptop'" in output
    assert "'Gaming laptop'" in output
    assert "1500.0" in output
    assert "3" in output
    assert output.strip() == (
        "Создан объект класса Product('Laptop', 'Gaming laptop', 1500.0, 3)"
    )
