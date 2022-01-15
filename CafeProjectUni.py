"""This is a final project for KHU-University Introduction of Programming course."""


class Cafe:
    def __init__(self, name):
        """"""
        self.name = name
        self.menu = {
            "Mocha": 4.25,
            "Caramel Latte": 4.25,
            "Espresso": 3,
            "Earl Grey": 3.25,
            "Green Tea": 3.25,
            "Orange Juice": 3.5,
            "Croissant": 4.45,
            "Muffin": 3.6
        }
        self.total_orders = []
        self.total_price = 0

    def request_menu(self):
        return self.menu

    def place_order(self, order):
        """"""
        self.total_orders.append(order)
        self.total_price += self.menu[order]
        return self.total_price


