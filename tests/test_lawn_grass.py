"""Тесты для класса LawnGrass."""

import pytest

from src.lawn_grass import LawnGrass


class TestLawnGrass:
    """Класс для тестирования LawnGrass."""

    def test_lawngrass_creation(self):
        """Тест создания экземпляра LawnGrass."""
        grass = LawnGrass(
            name="Premium Grass",
            description="Высококачественная газонная трава",
            price=49.99,
            quantity=100,
            country="Германия",
            germination_period="14 дней",
            color="Зеленый",
        )

        assert grass.name == "Premium Grass"
        assert grass.price == 49.99
        assert grass.quantity == 100
        assert grass.country == "Германия"
        assert grass.germination_period == "14 дней"
        assert grass.color == "Зеленый"

    def test_lawngrass_str(self):
        """Тест строкового представления LawnGrass."""
        grass = LawnGrass(
            name="Элитная трава",
            description="Для футбольных полей",
            price=89.99,
            quantity=50,
            country="Нидерланды",
            germination_period="10 дней",
            color="Темно-зеленый",
        )

        expected = "Элитная трава, 89.99 руб. Остаток: 50 шт."
        assert str(grass) == expected

    def test_lawngrass_repr(self):
        """Тест формального представления LawnGrass."""
        grass = LawnGrass(
            name="Стандарт",
            description="Для дачи",
            price=29.99,
            quantity=200,
            country="Россия",
            germination_period="21 день",
            color="Светло-зеленый",
        )

        expected = (
            "LawnGrass('Стандарт', 'Для дачи', 29.99, "
            "200, 'Россия', '21 день', 'Светло-зеленый')"
        )
        assert repr(grass) == expected

    def test_lawngrass_addition_same_type(self):
        """Тест сложения травы газонной одного типа."""
        grass1 = LawnGrass("Grass1", "Desc1", 30, 10, "Russia", "14 дней", "Green")
        grass2 = LawnGrass("Grass2", "Desc2", 40, 5, "Germany", "10 дней", "Dark Green")

        total = grass1 + grass2
        expected = (30 * 10) + (40 * 5)
        assert total == expected

    def test_lawngrass_addition_different_type(self):
        """Тест сложения травы газонной с другим типом продукта."""
        from src.smartphone import Smartphone

        grass = LawnGrass("Grass", "Desc", 30, 10, "Russia", "14 дней", "Green")
        smartphone = Smartphone("Phone", "Desc", 100, 2, 2.0, "M1", 64, "Black")

        with pytest.raises(TypeError, match="Нельзя складывать продукты разных типов"):
            _ = grass + smartphone
