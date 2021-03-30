from item_manager import ItemManager
from item.clothes_items import ClothesItems, Seasons
from item.sport_food import SportFood
from item.sport_equipment import SportEquipment
from item.item import Country, Material, Gender


class Example:
    def start(self):
        manager = ItemManager([
            ClothesItems("Cap", 100, Country.China, Material.Cotton, "Brand", Gender.Male, "XXL", "Golf",
                         Seasons.Summer, 21),
            SportEquipment("Suit", 2000, Country.USA, Material.Spandex, "Nike", Gender.Female, "XL", "Riding",
                           "F1000", True),
            SportFood("nutela", 10, Country.USA, "protein++", "ski", "Meat", "100kk")
        ])
        print("Sort by size")
        print("____________________________________________________\n")
        manager.show([Item for Item in manager.sort_by_size(True)])
        print("____________________________________________________\n")
        print("Sort by price")
        print("____________________________________________________\n")
        manager.show([Item for Item in manager.sort_by_price(True)])
        print("____________________________________________________\n")
        print("Search by type of sport")
        print("____________________________________________________\n")
        manager.show(manager.search("Golf"))
        print("____________________________________________________\n")
