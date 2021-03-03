class Conference:
    aim = "summing up"

    def __init__(self, day=None, time: str = None, name=None, amount_of_participants=0, price_of_ticket=0, city_of_holding=None):
        self.name = name
        self.amount_of_participants = amount_of_participants
        self.price_of_ticket = price_of_ticket
        self.city_of_holding = city_of_holding
        self.day = day
        self.time = time

    def __del__(self):
        pass

    def __str__(self):
        return f"Name: {self.name} \n" \
               f"Amount of participants: {self.amount_of_participants} \n" \
               f"Ticket price: {self.price_of_ticket} grn \n" \
               f"day: {self.day} \n" \
               f"City of holding: {self.city_of_holding} \n" \
               f"time: {self.time} \n" \
               f"aim: {Conference.aim} \n" \


    @staticmethod
    def set_aim():
        return Conference.aim

    @classmethod
    def print_aim(cls):
        print(Conference.aim)


def main():
    list_of_conferences = [Conference("Monday", "13:00", "Intel", 105, 328, "London"),
                           Conference("Tuesday", "14:00", "Amazon", 14, 38, "London"),
                           Conference("Friday", "17:00", "Microsoft", 15, 28, "London")]

    for i in list_of_conferences:
        print(i)


if __name__ == '__main__':
    main()
