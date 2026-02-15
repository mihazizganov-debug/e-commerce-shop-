import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_products():
    """Фикстура для создания тестовых продуктов."""
    return [
        Product("Товар 1", "Описание 1", 100.0, 5),
        Product("Товар 2", "Описание 2", 200.0, 3),
        Product("Товар 3", "Описание 3", 300.0, 7),
    ]


@pytest.fixture
def sample_category(sample_products):
    """Фикстура для создания тестовой категории."""
    return Category("Тестовая категория", "Описание категории", sample_products)


def test_category_creation(sample_category, sample_products):
    """Тест создания категории."""
    assert sample_category.name == "Тестовая категория"
    assert sample_category.description == "Описание категории"
    assert len(sample_category.products_list) == len(sample_products)


def test_category_counters():
    # Сбрасываем счетчики для теста
    Category.category_count = 0
    Category.product_count = 0

    # Создаем продукты
    product1 = Product("Товар 1", "Описание 1", 100.0, 5)
    product2 = Product("Товар 2", "Описание 2", 200.0, 3)

    # Создаем категорию
    category = Category("Категория 1", "Описание", [product1, product2])

    assert Category.category_count == 1
    assert Category.product_count == 2
    assert category.name == "Категория 1"  # Добавляем проверку

    # Создаем еще одну категорию
    product3 = Product("Товар 3", "Описание 3", 300.0, 7)
    Category("Категория 2", "Описание", [product3])

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_add_product(sample_category):
    """Тест добавления продукта в категорию."""
    new_product = Product("Новый товар", "Описание", 150.0, 2)
    sample_category.add_product(new_product)

    assert new_product in sample_category.products_list
    assert len(sample_category.products_list) == 4


def test_add_product_invalid_type(sample_category):
    """Тест добавления продукта неверного типа."""
    with pytest.raises(
        TypeError, match="Можно добавлять только продукты и их наследников"
    ):
        sample_category.add_product("Не продукт")  # type: ignore


def test_products_property(sample_category):
    """Тест свойства products (строковое представление)."""
    products_str = sample_category.products
    expected_lines = [
        "Товар 1, 100.0 руб. Остаток: 5 шт.",
        "Товар 2, 200.0 руб. Остаток: 3 шт.",
        "Товар 3, 300.0 руб. Остаток: 7 шт.",
    ]

    for expected in expected_lines:
        assert expected in products_str


def test_category_str(sample_category):
    """Тест строкового представления категории."""
    assert str(sample_category) == "Тестовая категория, количество продуктов: 15 шт."


def test_middle_price_with_products(sample_category):
    """Тест метода middle_price с товарами."""
    expected = (100.0 + 200.0 + 300.0) / 3  # 600 / 3 = 200
    assert sample_category.middle_price() == expected


def test_middle_price_with_empty_category():
    """Тест метода middle_price с пустой категорией."""
    empty_category = Category("Пустая категория", "Нет товаров", [])
    assert empty_category.middle_price() == 0.0


def test_category_with_mixed_prices():
    """Тест категории с разными ценами."""
    products = [
        Product("Дешевый", "Описание", 10.0, 1),
        Product("Средний", "Описание", 100.0, 1),
        Product("Дорогой", "Описание", 1000.0, 1),
    ]
    category = Category("Смешанная", "Описание", products)

    expected = (10.0 + 100.0 + 1000.0) / 3  # 1110 / 3 = 370
    assert category.middle_price() == expected


def test_middle_price_with_one_product():
    """Тест метода middle_price с одним товаром."""
    products = [Product("Один товар", "Описание", 500.0, 1)]
    category = Category("Одиночная", "Описание", products)

    assert category.middle_price() == 500.0
