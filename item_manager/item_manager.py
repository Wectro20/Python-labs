from item.item import Item


class ItemManager:
    def __init__(self, goods: list[Item]):
        self.goods = goods

    def sort_by_size(self, reverse: bool = False):
        return sorted(self.goods, key=lambda Item: Item.size, reverse=reverse)

    def sort_by_price(self, reverse: bool = False):
        return sorted(self.goods, key=lambda Item: Item.price, reverse=reverse)

    def search(self, type_of_sport: str = " "):
        search_list = []
        for i in self.goods:
            if i.type_of_sport == type_of_sport:
                search_list.append(i)
        return search_list

    def show(self, goods: list[Item] = None):
        if goods == None:
            print("goods is None")
        else:
            for i in goods:
                print(i)
