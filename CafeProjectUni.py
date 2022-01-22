"""This is a final project for KHU-University Introduction of Programming course."""
import random


class Cafe:
    def __init__(self, name) -> None:
        """This is the main function of Cafe's class and It contains menu and customer's name.
            Args:
            Returns:
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
            "Muffin": 3.6
        }
        self.total_orders = []
        self.total_price = 0

    def request_menu(self) -> dict:
        """
        """
        print(self.menu)

    def place_order(self, order) -> None:
        """
        """
        if order in self.menu:
            self.total_orders.append(order)
            self.total_price += self.menu[order]

    def request_bill(self, discount):
        final_cost = self.total_price * (1 - discount)
        print(f"Your name is: {self.name}")
        print("Your Bill : ")
        print(f"Total cost before discount: {self.total_price}")
        print(f"Your final cost: {final_cost}")
        print("Bye Bye!")


name = input("Hi!\nWelcome to our Cafe!\nWould you please enter your name?\n")
customer = Cafe(name)
menu_req = input("Do you want to see the menu?").lower()
if menu_req == "yes":
    customer.request_menu() # Todo : handle menu req.
while True:
    ordered = input("What do you want?: \n")
    order_status = True
    customer.place_order(ordered)
    if ordered == "place order" or ordered == "Place order":
        print("Ok! Please wait until your orders get ready!")
        game_req = input("Do you want to play a game? \n").lower()
        if game_req == "yes":
            x_loc = random.randint(1, 10)
            y_loc = random.randint(1, 10)
            counter = 0
            while True:
                game_loc = input(
                    "Welcome to the game!\nWe have a hidden ping-pong ball and you"
                    "have to guess the ball's location like: x,y \n"
                    "Note : the location's points is in the range of [1,10]: \n"
                )
                if game_loc == "end game":
                    break
                game_loc = game_loc.split(",")
                x = int(game_loc[0])
                y = int(game_loc[1])
                guess_status = ""
                game_done = False
                discount = 0
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
                    break
                counter += 1
                print(guess_status)
                if counter > 6:
                    print("Bruh! The game is over! gg!")
                if game_done == True:
                    if counter == 1:
                        discount = 1
                    elif counter <= 4 and counter > 1:
                        discount = 0.5
                    elif counter <= 6 and counter >4:
                        discount = 0.1
                customer.request_bill(discount)
