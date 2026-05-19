class Product:
    """
    Product class
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Product constructor
        :param name: name of the product
        :param description: description of the product
        :param price: price of the product
        :param quantity: quantity of the product
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
