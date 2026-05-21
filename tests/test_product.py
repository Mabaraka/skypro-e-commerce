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


def test_new_product_classmethod():
    """Проверка создания продукта через фабричный метод класса."""
    product_data = {"name": "Наушники", "description": "Беспроводные наушники", "price": 5000.0, "quantity": 15}
    product = Product.new_product(product_data)

    assert product.name == "Наушники"
    assert product.price == 5000.0
    assert product.quantity == 15


def test_price_setter_valid():
    """Проверка успешного изменения цены."""
    product = Product("Мышь", "Проводная", 1500.0, 8)
    product.price = 1800.0
    assert product.price == 1800.0


def test_price_setter_invalid_zero(capsys):
    """Проверка запрета на установку нулевой цены."""
    product = Product("Мышь", "Проводная", 1500.0, 8)
    product.price = 0

    assert product.price == 1500.0

    captured = capsys.readouterr()
    assert captured.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_price_setter_invalid_negative(capsys):
    """Проверка запрета на установку отрицательной цены."""
    product = Product("Мышь", "Проводная", 1500.0, 8)
    product.price = -100.0

    assert product.price == 1500.0

    captured = capsys.readouterr()
    assert captured.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_product_str(product_laptop):
    """Проверка строкового представления продукта."""
    assert str(product_laptop) == "Ноутбук, 70000.0 руб. Остаток: 3 шт. "


def test_product_add(product_laptop, product_mouse):
    """Проверка сложения двух продуктов (суммирование общей стоимости).

    Расчет: (70000.0 * 3) + (3000.0 * 10) = 210000.0 + 30000.0 = 240000.0
    """
    total_cost = product_laptop + product_mouse
    assert total_cost == 240000.0
