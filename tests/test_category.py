from src.category import Category
from src.product import Product


def test_category_initialization(sample_products):
    """Проверка корректной инициализации атрибутов категории."""
    category = Category("Электроника", "Гаджеты и техника", sample_products)

    assert category.name == "Электроника"
    assert category.description == "Гаджеты и техника"
    assert category.products == sample_products
    assert len(category.products) == 2


def test_category_counters_single_category(sample_products):
    """Проверка счетчиков при создании одной категории."""
    Category("Электроника", "Гаджеты и техника", sample_products)

    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_counters_multiple_categories(sample_products):
    """Проверка сквозного подсчета для нескольких категорий."""
    extra_products = [Product("Смартфон", "Флагман", 90000.0, 3)]

    Category("Электроника", "Гаджеты и техника", sample_products)
    Category("Смартфоны", "Мобильные телефоны", extra_products)

    # Всего создано 2 категории
    assert Category.category_count == 2
    # Всего продуктов во всех категориях: 2 + 1 = 3
    assert Category.product_count == 3


def test_category_with_empty_products():
    """Проверка создания категории без продуктов."""
    category = Category("Пустая категория", "Здесь ничего нет", [])

    assert category.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0
