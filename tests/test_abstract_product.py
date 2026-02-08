"""
Тесты для абстрактного класса BaseProduct.
"""

from abc import ABC

import pytest

from src.base_product import BaseProduct
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_base_product_is_abstract():
    """Проверяем, что BaseProduct является абстрактным классом."""
    assert issubclass(BaseProduct, ABC)

    # Нельзя создать экземпляр абстрактного класса
    with pytest.raises(TypeError):
        BaseProduct("Test", "Test", 100, 1)


def test_product_inherits_from_base_product():
    """Проверяем, что Product наследуется от BaseProduct."""
    assert issubclass(Product, BaseProduct)


def test_smartphone_inherits_from_product():
    """Проверяем, что Smartphone наследуется от Product."""
    assert issubclass(Smartphone, Product)


def test_lawn_grass_inherits_from_product():
    """Проверяем, что LawnGrass наследуется от Product."""
    assert issubclass(LawnGrass, Product)


def test_product_implements_abstract_methods():
    """Проверяем, что Product реализует все абстрактные методы."""
    product = Product("Test", "Test", 100.0, 1)  # Используем float!

    # Проверяем наличие методов
    assert hasattr(product, "__str__")
    assert hasattr(product, "__add__")
    assert hasattr(product, "new_product")
    assert hasattr(product, "price")

    # Проверяем, что методы работают
    assert isinstance(str(product), str)
    # price - это property, возвращающее float
    assert isinstance(product.price, (float, int))  # Может быть int или float
    assert product.price == 100.0


def test_abstract_methods_signatures():
    """Проверяем сигнатуры абстрактных методов."""
    # Проверяем, что методы объявлены как абстрактные
    assert BaseProduct.__init__.__isabstractmethod__
    assert BaseProduct.__str__.__isabstractmethod__
    assert BaseProduct.__add__.__isabstractmethod__
    assert BaseProduct.new_product.__isabstractmethod__
    assert BaseProduct.price.__isabstractmethod__
