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
        # Теперь products - это строка, а не список
        products_str = category.products
        assert isinstance(products_str, str)
        assert "Товар 1" in products_str
        assert "1000.0" in products_str
        assert "Товар 2" in products_str
        assert "2000.0" in products_str

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
        # Пустая строка для пустой категории
        assert empty_category.products == ""
        assert Category.category_count == 1
        assert Category.product_count == 0

    def test_category_with_single_product(self) -> None:
        """Тест категории с одним товаром."""
        category = Category("Одиночная", "Один товар", [self.product1])

        products_str = category.products
        assert "Товар 1" in products_str
        assert "1000.0" in products_str
        assert "5 шт." in products_str
        assert Category.product_count == 1

    def test_category_modification(self) -> None:
        """Тест изменения атрибутов категории после создания."""
        category = Category("Исходная", "Описание", [self.product1])

        # Меняем атрибуты
        category.name = "Измененная"
        category.description = "Новое описание"
        # Теперь нужно использовать add_product вместо append
        category.add_product(self.product2)  # Добавляем товар через метод

        assert category.name == "Измененная"
        assert category.description == "Новое описание"
        products_str = category.products
        assert "Товар 1" in products_str
        assert "Товар 2" in products_str
        # Счетчик должен увеличиться на 1
        assert Category.product_count == 2  # 1 + 1 = 2

    def test_multiple_categories_independence(self) -> None:
        """Тест независимости разных категорий."""
        category1 = Category("Кат1", "Описание1", [self.product1])
        category2 = Category("Кат2", "Описание2", [self.product2, self.product3])

        # Проверяем, что категории независимы
        assert category1.name != category2.name
        assert category1.products != category2.products

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

    # ДЗ 14.2 - новые тесты ниже

    def test_add_product_method(self) -> None:
        """Тест метода add_product (ДЗ 14.2)."""
        category = Category("Электроника", "Техника", [])
        initial_count = Category.product_count

        product = Product("Новый товар", "Описание", 5000.0, 2)
        category.add_product(product)

        # Проверяем что счетчик увеличился
        assert Category.product_count == initial_count + 1
        # Проверяем что товар добавился в список
        products_str = category.products
        assert "Новый товар, 5000.0 руб. Остаток: 2 шт." in products_str

    def test_products_property_format(self) -> None:
        """Тест геттера products с правильным форматированием (ДЗ 14.2)."""
        product1 = Product("Товар1", "Описание1", 1000.0, 5)
        product2 = Product("Товар2", "Описание2", 2000.0, 3)
        category = Category("Категория", "Описание", [product1, product2])

        products_str = category.products

        # Проверяем формат
        expected_lines = [
            "Товар1, 1000.0 руб. Остаток: 5 шт.",
            "Товар2, 2000.0 руб. Остаток: 3 шт.",
        ]
        for expected_line in expected_lines:
            assert expected_line in products_str

        # Проверяем что строки разделены новой строкой
        lines = products_str.split("\n")
        assert len(lines) == 2

    def test_private_products_attribute(self) -> None:
        """Тест приватности атрибута __products (ДЗ 14.2)."""
        product = Product("Товар", "Описание", 100.0, 10)
        category = Category("Категория", "Описание", [product])

        # Прямой доступ к приватному атрибуту должен вызывать ошибку
        with pytest.raises(AttributeError):
            _ = category.__products  # Это вызовет AttributeError

        # Но работает как property
        assert isinstance(category.products, str)

    # ДЗ 15.1 - новые тесты ниже

    def test_category_str_method(self) -> None:
        """Тест метода __str__ для Category."""
        product1 = Product("Товар1", "Описание1", 100.0, 5)
        product2 = Product("Товар2", "Описание2", 200.0, 3)
        category = Category("Категория", "Описание", [product1, product2])

        # 5 + 3 = 8 продуктов
        assert str(category) == "Категория, количество продуктов: 8 шт."

    def test_category_str_empty(self) -> None:
        """Тест метода __str__ для пустой категории."""
        category = Category("Пустая", "Описание", [])
        assert str(category) == "Пустая, количество продуктов: 0 шт."

    def test_products_property_uses_str(self) -> None:
        """Тест что геттер products использует __str__ продуктов."""
        product = Product("Телефон", "Смартфон", 10000.0, 10)
        category = Category("Категория", "Описание", [product])

        products_str = category.products
        expected = "Телефон, 10000.0 руб. Остаток: 10 шт."
        assert products_str == expected
