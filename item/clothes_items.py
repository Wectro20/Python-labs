from enum import Enum
from .item import Item
from .item import Country, Material, Gender


class Seasons(Enum):
    Spring = 0
    Summer = 1
    Autumn = 2
    Winter = 3


class ClothesItems(Item):
    def __init__(self, name: str = " ", price: float = 0.0, country: Country = None, material: Material = None,
                 brand: str = " ", gender: Gender = None, size: str = " ", type_of_sport: str = " ",
                 season: Seasons = None, temperature: float = 0.0):
        super().__init__(price=price, country=country, material=material, brand=brand, gender=gender, size=size,
                         type_of_sport=type_of_sport, name=name)
        self.season = season
        self.temperature = temperature

    def __str__(self):
        return f"Name: {self.name}\n"\
               f"Price: {self.price}\n " \
               f"Country: {self.country}\n " \
               f"Material: {self.material}\n " \
               f"Brand: {self.brand}\n" \
               f"Gender: {self.gender}\n " \
               f"Size: {self.size}\n " \
               f"Type of sport: {self.type_of_sport}\n " \
               f"Season: {self.season}\n " \
               f"Temperature: {self.temperature}\n "

    def __repr__(self):
        return f"Name: {self.name}\n"\
               f"Price: {self.price}\n " \
               f"Country: {self.country}\n " \
               f"Material: {self.material}\n " \
               f"Brand: {self.brand}\n" \
               f"Gender: {self.gender}\n " \
               f"Size: {self.size}\n " \
               f"Type of sport: {self.type_of_sport}\n " \
               f"Season: {self.season}\n " \
               f"Temperature: {self.temperature}\n"
