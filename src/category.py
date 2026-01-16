class Category:
    """Класс для представления категории товаров в интернет-магазине."""

    # Атрибуты класса
    category_count = 0  # Общее количество категорий
    product_count = 0  # Общее количество товаров

    def __init__(self, name: str, description: str, products: list):
        """Инициализирует новый экземпляр класса Category."""
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем счетчики
        Category.category_count += 1
        Category.product_count += len(products)
