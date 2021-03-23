from enum import Enum


class Country(Enum):
    China = 0
    USA = 1
    Vietnam = 2


class Material(Enum):
    Cotton = 0
    Spandex = 1
    Polyester = 2


class Gender(Enum):
    Male = 0
    Female = 1
    Undefined = 2


class Item:
    def __init__(self, price: float = 0.0, country: Country = None, material: Material = None, brand: str = " ",
                 gender: Gender = None, size: str = " ", type_of_sport: str = " ", name: str = " "):
        self.price = price
        self.country = country
        self.material = material
        self.brand = brand
        self.gender = gender
        self.size = size
        self.type_of_sport = type_of_sport
        self.name = name

    def __str__(self):
        return f"Price: {self.price}\n " \
               f"Country: {self.country}\n " \
               f"Material: {self.material}\n " \
               f"Brand: {self.brand}\n" \
               f"Gender: {self.gender}\n " \
               f"Size: {self.size}\n " \
               f"Type of sport: {self.type_of_sport}\n " \
               f"Name: {self.name}\n"

