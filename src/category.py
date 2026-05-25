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
        if not isinstance(product, Product):
            raise TypeError
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Product property
        :return: string of the products"
        """
        return "".join(f"{str(product)}\n" for product in self.__products)

    def __str__(self) -> str:
        quantity_all_products = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {quantity_all_products} шт."

    def get_average_price(self) -> float:
        try:
            sum = 0
            for product in self.__products:
                sum += product.price
            return sum / len(self.__products)
        except ZeroDivisionError:
            return 0
