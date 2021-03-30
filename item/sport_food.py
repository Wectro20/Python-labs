from .item import Item
from .item import Country


class SportFood(Item):
    def __init__(self, name: str = " ", price: float = 0.0, country: Country = None, brand: str = " ",
                 type_of_sport: str = " ", main_component: str = None, nutritional_value: str = None):
        super().__init__(price=price, country=country, brand=brand, type_of_sport=type_of_sport, name=name)
        self.main_component = main_component
        self.nutritional_value = nutritional_value

    def __str__(self):
        return f"Name: {self.name}\n"\
               f"Price: {self.price}\n " \
               f"Country: {self.country}\n " \
               f"Brand: {self.brand}\n" \
               f"Type of sport: {self.type_of_sport}\n " \
               f"Main component: {self.main_component}\n " \
               f"Nutritional value: {self.nutritional_value}\n "

    def __repr__(self):
        return f"Name: {self.name}\n"\
               f"Price: {self.price}\n " \
               f"Country: {self.country}\n " \
               f"Brand: {self.brand}\n" \
               f"Type of sport: {self.type_of_sport}\n " \
               f"Main component: {self.main_component}\n " \
               f"Nutritional value: {self.nutritional_value}\n"
