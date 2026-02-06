"""Тесты для класса Smartphone."""

import pytest

from src.smartphone import Smartphone


class TestSmartphone:
    """Класс для тестирования Smartphone."""

    def test_smartphone_creation(self):
        """Тест создания экземпляра Smartphone."""
        smartphone = Smartphone(
            name="iPhone 15",
            description="Новый iPhone",
            price=999.99,
            quantity=10,
            efficiency=3.8,
            model="15 Pro",
            memory=256,
            color="Black",
        )

        assert smartphone.name == "iPhone 15"
        assert smartphone.price == 999.99
        assert smartphone.quantity == 10
        assert smartphone.efficiency == 3.8
        assert smartphone.model == "15 Pro"
        assert smartphone.memory == 256
        assert smartphone.color == "Black"

    def test_smartphone_str(self):
        """Тест строкового представления Smartphone."""
        smartphone = Smartphone(
            name="Samsung Galaxy",
            description="Android smartphone",
            price=799.99,
            quantity=5,
            efficiency=3.5,
            model="S23",
            memory=128,
            color="White",
        )

        expected = "Samsung Galaxy, 799.99 руб. Остаток: 5 шт."
        assert str(smartphone) == expected

    def test_smartphone_repr(self):
        """Тест формального представления Smartphone."""
        smartphone = Smartphone(
            name="Xiaomi",
            description="Chinese smartphone",
            price=299.99,
            quantity=20,
            efficiency=2.8,
            model="Redmi Note",
            memory=64,
            color="Blue",
        )

        expected = (
            "Smartphone('Xiaomi', 'Chinese smartphone', 299.99, "
            "20, 2.8, 'Redmi Note', 64, 'Blue')"
        )
        assert repr(smartphone) == expected

    def test_smartphone_addition_same_type(self):
        """Тест сложения смартфонов одного типа."""
        smartphone1 = Smartphone("Phone1", "Desc1", 100, 2, 2.0, "M1", 64, "Black")
        smartphone2 = Smartphone("Phone2", "Desc2", 200, 3, 2.5, "M2", 128, "White")

        total = smartphone1 + smartphone2
        expected = (100 * 2) + (200 * 3)
        assert total == expected

    def test_smartphone_addition_different_type(self):
        """Тест сложения смартфона с другим типом продукта."""
        from src.lawngrass import LawnGrass

        smartphone = Smartphone("Phone", "Desc", 100, 2, 2.0, "M1", 64, "Black")
        grass = LawnGrass("Grass", "Desc", 30, 4, "Russia", "14 дней", "Green")

        with pytest.raises(TypeError, match="Нельзя складывать продукты разных типов"):
            _ = smartphone + grass
