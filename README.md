# 🛒 E-commerce Shop Project

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/mihazizganov-debug/e-commerce-shop-)

Проект интернет-магазина на Python.

## 📋 Домашнее задание 14.1

### ✅ Реализовано:

#### 1. **Класс Product** (товар):
   - Атрибуты: `name`, `description`, `price`, `quantity`
   - Аннотации типов для всех параметров

#### 2. **Класс Category** (категория товаров):
   - Атрибуты: `name`, `description`, `products` (список объектов Product)
   - Атрибуты класса: `category_count`, `product_count`
   - Автоматический подсчет при создании объектов

#### 3. **Тестирование**:
   - 10 тестов для класса Product
   - 10 тестов для класса Category
   - Проверка инициализации объектов
   - Проверка подсчета категорий и товаров
   - Покрытие кода тестами: **100%**

#### 4. **Верификация**:
   - ✅ Код из файла `14.1_main.py` запускается без ошибок
   - ✅ Соответствие PEP 8 (flake8 проверка)
   - ✅ Аннотации типов (mypy проверка)
   - ✅ Все 20 тестов проходят успешно

## 🚀 Как запустить проект:

```bash
# 1. Клонирование репозитория
git clone https://github.com/mihazizganov-debug/e-commerce-shop-.git
cd e-commerce-shop-

# 2. Установка Poetry (если еще не установлен)
# Для Windows:
pip install poetry

# 3. Установка зависимостей
poetry install

# 4. Активация виртуального окружения
poetry shell

# 5. Запуск основного кода
python main.py

# 6. Запуск тестов
pytest tests/

# 7. Проверка покрытия
pytest tests/ --cov=src

# 8. Проверка стиля кода
flake8 src/ tests/ main.py
```

## Структура проекта
e-commerce-shop-/
├── main.py                   # Основной файл с демонстрационным кодом
├── src/
│   ├── __init__.py           # Инициализация пакета
│   ├── product.py            # Класс Product
│   └── category.py           # Класс Category
├── tests/
│   ├── test_product.py       # Тесты для Product
│   └── test_category.py      # Тесты для Category
├── .flake8                   # Конфигурация flake8
├── .gitignore                # Игнорируемые файлы
├── poetry.lock               # Точные версии зависимостей
├── pyproject.toml            # Конфигурация проекта и зависимости
└── README.md                 # Документация