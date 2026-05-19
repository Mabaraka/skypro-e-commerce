from src.product import Product


def test_product_initialization():
    """Проверка корректной инициализации объекта."""
    product = Product("Ноутбук", "Мощный игровой ноутбук", 75000.0, 5)

    assert product.name == "Ноутбук"
    assert product.description == "Мощный игровой ноутбук"
    assert product.price == 75000.0
    assert product.quantity == 5


def test_product_types():
    """Проверка типов данных после инициализации."""
    product = Product("Телефон", "Смартфон", 29990.50, 10)

    assert isinstance(product.name, str)
    assert isinstance(product.description, str)
    assert isinstance(product.price, float)
    assert isinstance(product.quantity, int)
