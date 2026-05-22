import pytest

from src.category import Category
from src.product import LawnGrass
from src.product import Product
from src.product import Smartphone


@pytest.fixture(autouse=True)
def reset_category_counters():
    """Фикстура для сброса счетчиков перед каждым тестом.
    Это гарантирует, что тесты изолированы и независимы друг от друга.
    """
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_products():
    """Фикстура для создания тестового списка продуктов."""
    return [
        Product("Ноутбук", "Игровой", 75000.0, 5),
        Product("Мышь", "Беспроводная", 3000.0, 10),
    ]


@pytest.fixture
def product_laptop():
    """Фикстура для создания первого продукта."""
    return Product("Ноутбук", "Игровой", 70000.0, 3)


@pytest.fixture
def product_mouse():
    """Фикстура для создания второго продукта."""
    return Product("Мышь", "Беспроводная", 3000.0, 10)


@pytest.fixture
def smartphone_iphone():
    return Smartphone(
        name="iPhone 15",
        description="Флагман",
        price=100000.0,
        quantity=5,
        efficiency=4.5,
        model="15 Pro",
        memory=256,
        color="Titanium",
    )


@pytest.fixture
def smartphone_samsung():
    return Smartphone(
        name="Samsung S24",
        description="Флагман Android",
        price=90000.0,
        quantity=3,
        efficiency=4.3,
        model="S24 Ultra",
        memory=512,
        color="Black",
    )


@pytest.fixture
def grass_shady():
    return LawnGrass(
        name="Тень-Экстра",
        description="Трава для тенистых мест",
        price=500.0,
        quantity=20,
        country="Германия",
        germination_period="14 дней",
        color="Темно-зеленый",
    )
