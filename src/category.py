from src.product import Product


class Category:
    """
    Category class
    """

    category_count = 0
    product_count = 0

    name: str
    description: str
    __products: list[Product]

    def __init__(self, name: str, description: str, products: list[Product]):
        """
        Category constructor
        :param name: name of the category
        :param description: description of the category
        :param products: list of products
        """
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        """
        Add product to the category
        :param product: product to be added
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Product property
        :return: string of the products"
        """
        return "".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт. \n" for product in self.__products
        )
