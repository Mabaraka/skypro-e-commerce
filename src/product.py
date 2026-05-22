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
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, p_dict: dict) -> Product:
        """
        Product constructor
        :param p_dict: dictionary with product information
        :return: product instance
        """
        return cls(**p_dict)

    @property
    def price(self) -> float:
        """
        Product price getter
        :return: price of the product
        """
        return self.__price

    @price.setter
    def price(self, value: float):
        """
        Product price setter
        :param value: new price of the product, must be greater than 0
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт. "

    def __add__(self, other: Product) -> float:
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов!")
        return (self.__price * self.quantity) + (other.__price * other.quantity)


class Smartphone(Product):
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
