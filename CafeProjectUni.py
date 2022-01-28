"""Cafe Project Code for KHU Intro to computer course"""
# --------------------------- Import libraries and functions --------------------------
import numpy as np
import random

# -------------------------------- Cafe Class --------------------------------
class Cafe:
    """Cafe Class"""

    def __init__(self, name: str) -> None:
        """Main function for Cafe Class.

        Args:
            Self: self represents the instance of the class.
            name (Type: string): Name of the customer.
        """
        self.name = name
        self.menu = {
            "Mocha": 4.25,
            "Caramel Latte": 4.25,
            "Espresso": 3,
            "Earl Grey": 3.25,
            "Green Tea": 3.25,
            "Orange Juice": 3.5,
            "Croissant": 4.45,
            "Muffin": 3.6,
        }
        self.total_orders = []
        self.total_price = 0

    def request_menu(self) -> str:
        """This function prints menu items."""
        [print(key, ":", value) for key, value in self.menu.items()]

    def place_order(self, order: str) -> None:
        """A function to save prices and orders if the orders exists in self.menu.

        Args:
            Self: self represents the instance of the class.
            order (Type: string): orders.
        """
        if order in self.menu:
            self.total_orders.append(order)
            self.total_price += self.menu[order]

    def request_bill(self, discount: float) -> str:
        """This function prints bill

        Args:
            Self: self represents the instance of the class.
            discount (Type: float): discount of bill that is determined from game.
        """
        values, counts = np.unique(self.total_orders, return_counts=True)
        final_cost = self.total_price * (1 - discount)
        print("============================")
        print(f"Your name is: {self.name}")
        print("Your Bill : ")
        temp = 0
        while temp < len(values):
            print("    ", values[temp], ":", counts[temp])
            temp += 1
        print(f"Total cost before discount: {self.total_price}")
        print(f"Your final cost: {final_cost}")
        print("Bye Bye!")
        print("============================")


# -------------------------------- Main App --------------------------------
name = input("Hi!\nWelcome to our Cafe!\nWould you please enter your name?\n")
customer = Cafe(name)
menu_req = input("Do you want to see the menu?\n").lower()
if menu_req == "yes":
    customer.request_menu()
elif menu_req == "no":
    pass
else:
    raise Exception("Please Enter valid input!")
while True:
    ordered = input("What do you want?: \n")
    order_status = True
    customer.place_order(ordered)
    if ordered == "place order" or ordered == "Place order":
        print("Ok! Please wait until your orders get ready!")
        game_req = input("Do you want to play a game? \n").lower()
        discount = 0
        if game_req == "yes":
            # -------------------------------- Game --------------------------------
            x_loc = random.randint(1, 10)
            y_loc = random.randint(1, 10)
            counter = 0
            print(
                "Welcome to the game!\nWe have a hidden ping-pong ball and you"
                "have to guess the ball's location like: x,y \n"
                "Note : the location's points is in the range of [1,10]: \n"
            )
            while True:
                game_loc = input()
                if game_loc == "end game":
                    customer.request_bill(0)
                    exit()
                game_loc = game_loc.split(",")
                x = int(game_loc[0])
                y = int(game_loc[1])
                guess_status = "Hint: "
                game_done = False
                if x > x_loc:
                    guess_status += "Left "
                elif x < x_loc:
                    guess_status += "Right "
                if y > y_loc:
                    guess_status += "Down"
                elif y < y_loc:
                    guess_status += "Up"
                if y_loc == y and x_loc == x:
                    print("You nailed it! Success!")
                    game_done = True
                if game_done == False:
                    print(guess_status + "\nTry again:")
                counter += 1
                if counter > 6:
                    print("Bruh! The game is over! gg!")
                if game_done == True:
                    if counter == 1:
                        discount = 1
                    elif counter <= 4 and counter > 1:
                        discount = 0.5
                    elif counter <= 6 and counter > 4:
                        discount = 0.1
                    customer.request_bill(discount)
                    exit()
        if game_req == "no":
            customer.request_bill(discount)
            exit()
