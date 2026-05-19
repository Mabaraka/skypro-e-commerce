from src.product import Product


class Category:
    """
    Category class
    """

    category_count = 0
    product_count = 0

    name: str
    description: str
    products: list[Product]

    def __init__(self, name: str, description: str, products: list[Product]):
        """
        Category constructor
        :param name: name of the category
        :param description: description of the category
        :param products: list of products
        """
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
