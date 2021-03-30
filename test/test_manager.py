import unittest
from item_manager import ItemManager
from item.clothes_items import ClothesItems, Seasons
from item.sport_food import SportFood
from item.sport_equipment import SportEquipment
from item.item import Country, Material, Gender


class ManagerTest(unittest.TestCase):
    item_list = [
        ClothesItems("Cap", 100, Country.China, Material.Cotton, "Brand", Gender.Male, "XXL", "Golf",
                     Seasons.Summer, 21),
        SportEquipment("Suit", 2000, Country.USA, Material.Spandex, "Nike", Gender.Female, "XL", "Riding",
                       "F1000", True),
        SportFood("nutela", 10, Country.USA, "protein++", "ski", "Meat", "100kk")
    ]

    def test_sort_by_price_increment(self):
        self.assertEqual(sorted(ManagerTest.item_list, key=lambda i: i.price, reverse=False),
                         ItemManager(ManagerTest.item_list).sort_by_price(False))

    def test_sort_by_price_decrement(self):
        self.assertEqual(sorted(ManagerTest.item_list, key=lambda i: i.price, reverse=True),
                         ItemManager(ManagerTest.item_list).sort_by_price(True))

    def test_sort_by_size_increment(self):
        self.assertEqual(sorted(ManagerTest.item_list, key=lambda i: i.size, reverse=False),
                         ItemManager(ManagerTest.item_list).sort_by_size(False))

    def test_sort_by_size_decrement(self):
        self.assertEqual(sorted(ManagerTest.item_list, key=lambda i: i.size, reverse=True),
                         ItemManager(ManagerTest.item_list).sort_by_size(True))

    def test_search_by_type_of_sport(self):
        search_list = []
        for i in ManagerTest.item_list:
            if i.type_of_sport == "Golf":
                search_list.append(i)
        self.assertEqual(search_list, ItemManager(ManagerTest.item_list).search("Golf"))
