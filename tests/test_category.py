import pytest

from src.category import Category
from src.product import Product


class TestCategory:
    """Тестирование функциональности класса Category."""

    def setup_method(self) -> None:
        """Подготовка тестовых данных перед каждым тестом."""
        # Сбрасываем счетчики
        Category.category_count = 0
        Category.product_count = 0

        # Создаем тестовые продукты
        self.product1 = Product("Товар 1", "Описание 1", 1000.0, 5)
        self.product2 = Product("Товар 2", "Описание 2", 2000.0, 3)
        self.product3 = Product("Товар 3", "Описание 3", 3000.0, 2)

    def test_category_initialization(self) -> None:
        """Тест инициализации категории."""
        category = Category(
            "Электроника", "Технические устройства", [self.product1, self.product2]
        )

        assert category.name == "Электроника"
        assert category.description == "Технические устройства"
        assert len(category.products) == 2
        assert category.products[0].name == "Товар 1"
        assert category.products[1].price == 2000.0

    def test_category_count_increases(self) -> None:
        """Тест увеличения счетчика категорий."""
        assert Category.category_count == 0

        category1 = Category("Кат1", "Описание1", [self.product1])
        assert Category.category_count == 1

        category2 = Category("Кат2", "Описание2", [self.product2])
        assert Category.category_count == 2

        # Проверяем доступ через объекты
        assert category1.category_count == 2
        assert category2.category_count == 2

    def test_product_count_increases(self) -> None:
        """Тест увеличения счетчика товаров."""
        assert Category.product_count == 0

        # Категория с 2 товарами
        category1 = Category("Кат1", "Описание1", [self.product1, self.product2])
        assert Category.product_count == 2

        # Категория с 1 товаром
        category2 = Category("Кат2", "Описание2", [self.product3])
        assert Category.product_count == 3  # 2 + 1 = 3

        # Проверяем доступ через объекты
        assert category1.product_count == 3
        assert category2.product_count == 3

    def test_empty_category(self) -> None:
        """Тест создания пустой категории."""
        empty_category = Category("Пустая", "Нет товаров", [])

        assert empty_category.name == "Пустая"
        assert len(empty_category.products) == 0
        assert Category.category_count == 1
        assert Category.product_count == 0

    def test_category_with_single_product(self) -> None:
        """Тест категории с одним товаром."""
        category = Category("Одиночная", "Один товар", [self.product1])

        assert len(category.products) == 1
        assert category.products[0].quantity == 5
        assert Category.product_count == 1

    def test_category_with_many_products(self) -> None:
        """Тест категории со многими товарами."""
        many_products = [
            Product(f"Товар {i}", f"Описание {i}", i * 100.0, i) for i in range(1, 11)
        ]  # 10 товаров

        category = Category("Много товаров", "Большая категория", many_products)

        assert len(category.products) == 10
        assert Category.product_count == 10
        assert category.products[4].name == "Товар 5"

    def test_category_products_are_actual_objects(self) -> None:
        """Тест, что продукты в категории - настоящие объекты Product."""
        category = Category("Тест", "Описание", [self.product1])

        product_in_category = category.products[0]

        # Проверяем, что это тот же объект
        assert product_in_category is self.product1
        assert product_in_category.name == "Товар 1"
        assert product_in_category.price == 1000.0

    def test_category_modification(self) -> None:
        """Тест изменения атрибутов категории после создания."""
        category = Category("Исходная", "Описание", [self.product1])

        # Меняем атрибуты
        category.name = "Измененная"
        category.description = "Новое описание"
        category.products.append(self.product2)  # Добавляем товар

        assert category.name == "Измененная"
        assert category.description == "Новое описание"
        assert len(category.products) == 2
        # Счетчики не должны измениться при изменении списка после создания
        assert (
            Category.product_count == 1
        )  # Все еще 1, т.к. счетчик считался при создании

    def test_multiple_categories_independence(self) -> None:
        """Тест независимости разных категорий."""
        category1 = Category("Кат1", "Описание1", [self.product1])
        category2 = Category("Кат2", "Описание2", [self.product2, self.product3])

        # Проверяем, что категории независимы
        assert category1.name != category2.name
        assert len(category1.products) != len(category2.products)
        assert category1.products[0] is not category2.products[0]

    def test_category_class_attributes_access(self) -> None:
        """Тест доступа к атрибутам класса разными способами."""
        category = Category("Тест", "Описание", [self.product1, self.product2])

        # Через класс
        assert Category.category_count == 1
        assert Category.product_count == 2

        # Через объект
        assert category.category_count == 1
        assert category.product_count == 2

        # Значения должны совпадать
        assert category.category_count == Category.category_count
        assert category.product_count == Category.product_count
