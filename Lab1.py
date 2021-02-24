# Три додаткових поля, які найкраще описують даний клас
# Конструктор (із вказаними дефолтними значеннями)
# Деструктор
# Метод, що повертає стрічкове представлення класу (__str__())
# Статичне поле
# Статичний метод, що повертає значення статичного поля
# В main() методі визначіть 3 об’єкти типу із завдання (з-за допомогою передачі різної кількості параметрів) та виведіть інформацію про них з-за допомогою методу з пункту 4 в консоль


# 18
# Створити клас “Конференція”  котрий містить поля:
# - назва
# - кількість учасників
# - ціна квитка
# - місто проведення

class Conference:

    day = "Monday"
    time = 13.00
    aim = "summing_up"

    def __init__(self, name = None, amount_of_participants = 0, price_of_ticket = 0, city_of_holding = None):
        self.name = name
        self.amount_of_participants = amount_of_participants
        self.price_of_ticket = price_of_ticket
        self.city_of_holding = city_of_holding

    def __del__(self):
        print("Object deleted")

    def __str__(self):
        return f"Name: {self.name} \nAmount of participants: {self.amount_of_participants} \nTicket price: {self.price_of_ticket} grn \nCity of holding: {self.city_of_holding}"

    static_pole = "static"

    @staticmethod
    def static_method(static_pole):
        return f"static method called {static_pole}"

if __name__ == '__main__':

       conference = Conference("SoftServe", 105, 328, "Lviv")
       print(conference.__str__())

