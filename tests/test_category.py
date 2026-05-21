from src.category import Category
from src.product import Product


def test_category_initialization(sample_products):
    """Проверка корректной инициализации атрибутов категории."""
    category = Category("Электроника", "Гаджеты и техника", sample_products)

    assert category.name == "Электроника"
    assert category.description == "Гаджеты и техника"


def test_category_products_property(sample_products):
    """Проверка геттера products, который возвращает строковое представление."""
    category = Category("Электроника", "Гаджеты и техника", sample_products)

    expected_output = "Ноутбук, 75000.0 руб. Остаток: 5 шт. \n" "Мышь, 3000.0 руб. Остаток: 10 шт. \n"
    assert category.products == expected_output


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

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_category_with_empty_products():
    """Проверка создания категории без продуктов."""
    category = Category("Пустая категория", "Здесь ничего нет", [])

    assert category.products == ""
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_add_product(sample_products):
    """Проверка метода add_product и корректного увеличения счетчика продуктов."""
    category = Category("Электроника", "Гаджеты и техника", sample_products)
    new_product = Product("Клавиатура", "Механическая", 5000.0, 7)

    category.add_product(new_product)

    assert Category.product_count == 3
    assert "Клавиатура, 5000.0 руб. Остаток: 7 шт. \n" in category.products


def test_category_str(sample_products):
    """Проверка строкового представления категории.

    В фикстуре sample_products: 5 ноутбуков + 10 мышей = 15 шт. всего.
    """
    category = Category("Электроника", "Гаджеты", sample_products)

    assert str(category) == "Электроника, количество продуктов: 15 шт."


def test_category_str_empty():
    """Проверка строкового представления пустой категории."""
    category = Category("Пустая", "Без товаров", [])

    assert str(category) == "Пустая, количество продуктов: 0 шт."
