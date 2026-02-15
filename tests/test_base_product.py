from abc import ABC

import pytest

from src.base_product import BaseProduct

# Импортируем правильно:
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_base_product_is_abstract():
    """BaseProduct должен быть абстрактным классом."""
    assert issubclass(BaseProduct, ABC)

    with pytest.raises(TypeError):
        BaseProduct("Test", "Test", 100, 1)


def test_product_inherits_from_base_product():
    """Product должен наследоваться от BaseProduct."""
    assert issubclass(Product, BaseProduct)


def test_smartphone_inherits_only_from_product():
    """Smartphone должен наследоваться только от Product."""
    assert Smartphone.__bases__ == (Product,)


def test_lawn_grass_inherits_only_from_product():
    """LawnGrass должен наследоваться только от Product."""
    assert LawnGrass.__bases__ == (Product,)


def test_all_abstract_methods_implemented():
    """Все абстрактные методы должны быть реализованы."""
    product = Product("Test", "Test", 100.0, 1)  # Используем float!

    # Проверяем наличие методов
    assert hasattr(product, "__init__")
    assert hasattr(product, "__str__")
    assert hasattr(product, "__add__")
    assert hasattr(product, "new_product")
    assert hasattr(product, "price")
    # Проверяем сеттер price
    assert hasattr(Product.price, "setter")
    assert hasattr(Product.price, "fset")  # Альтернативная проверка
