import pytest

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


def test_smartphone_initialization(smartphone_iphone):
    """Проверка создания и специфичных атрибутов смартфона."""
    assert smartphone_iphone.name == "iPhone 15"
    assert smartphone_iphone.efficiency == 4.5
    assert smartphone_iphone.model == "15 Pro"
    assert smartphone_iphone.memory == 256
    assert smartphone_iphone.color == "Titanium"
    assert isinstance(smartphone_iphone, Product)


def test_lawn_grass_initialization(grass_shady):
    """Проверка создания и специфичных атрибутов травы."""
    assert grass_shady.name == "Тень-Экстра"
    assert grass_shady.country == "Германия"
    assert grass_shady.germination_period == "14 дней"
    assert grass_shady.color == "Темно-зеленый"
    assert isinstance(grass_shady, Product)


def test_add_smartphones(smartphone_iphone, smartphone_samsung):
    """Проверка сложения двух смартфонов одного типа.

    Расчет: (100000.0 * 5) + (90000.0 * 3) = 500000 + 270000 = 770000.0
    """
    assert smartphone_iphone + smartphone_samsung == 770000.0


def test_add_different_types_raises_error(smartphone_iphone, grass_shady):
    """Проверка, что сложение разных классов (Смартфон + Трава) вызывает TypeError."""
    with pytest.raises(TypeError) as exc_info:
        _ = smartphone_iphone + grass_shady

    assert str(exc_info.value) == "Нельзя складывать товары разных типов!"


def test_add_subclass_and_parent_raises_error(smartphone_iphone, product_laptop):
    """Проверка, что сложение Смартфона и базового Продукта вызывает TypeError."""
    with pytest.raises(TypeError) as exc_info:
        _ = smartphone_iphone + product_laptop

    assert str(exc_info.value) == "Нельзя складывать товары разных типов!"
