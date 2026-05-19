import pytest

from src.category import Category
from src.product import Product


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
