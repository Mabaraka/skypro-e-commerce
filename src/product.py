from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from src.mixins import LogInitMixin


class BaseProduct(ABC):
    """
    BaseProduct abstract class
    """

    def __init__(self, **kwargs):
        super().__init__()

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price: float) -> None:
        pass

    @abstractmethod
    def __add__(self, other: BaseProduct) -> float:
        pass


class Product(BaseProduct, LogInitMixin):
    """
    Product class
    """

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int, **kwargs) -> None:
        # Передаём kwargs дальше (LogInitMixin -> BaseProduct -> object)
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        super().__init__(name=name, description=description, price=price, quantity=quantity, **kwargs)

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
    def price(self, new_price: float):
        """
        Product price setter
        :param new_price: new price of the product, must be greater than 0
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

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
    ) -> None:
        # Специфичные для Smartphone параметры НЕ передаём наверх —
        # BaseProduct их не знает и **kwargs не пробросит дальше.
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name=name, description=description, price=price, quantity=quantity)


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
    ) -> None:
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name=name, description=description, price=price, quantity=quantity)
