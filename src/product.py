from __future__ import annotations


class Product:
    """
    Product class
    """

    name: str
    description: str
    __price: float
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

    @classmethod
    def new_product(cls, p_dict: dict) -> Product:
        return cls(**p_dict)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value
