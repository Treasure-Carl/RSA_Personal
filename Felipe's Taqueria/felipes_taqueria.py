from pprint import pprint
# def order():
menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
# print(menu.items())
# print(menu.keys())
# print(menu.values())
# functions to place order and calculate prices
def place_order(menu):
    total_price = 0
    while True:
        order = input('What is your order: ')
        if order.lower() == 'done':
            break
        if order in menu:
            total_price += menu[order]
            print(f"{order.capitalize()} added to the order. Total price: ${total_price:.2f}")
        else:
            print("Sorry, that item is not on the menu. Please choose again.")
place_order(menu)
