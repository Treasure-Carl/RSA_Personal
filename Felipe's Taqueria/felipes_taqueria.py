from pprint import pprint
# def order():
menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
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
        order = input('What is your order: ').strip()
        if order.lower() == 'done':
            break 
        for ch in order:
            if ch.lower() or ch.isupper() in order:
                # for ch in order:
                #     if ch.replace(" ", "") == ch.replace(" ", ""):
                #         order.append(order.capitalize())
                order = order.capitalize()
        # for order in menu:
        #     if order.replace(" ", "") == order.replace(" ", ""):
        #         order.append(order.capitalize())
        #         found = True
        #         break
        #     if not found:
        #         order = input("Sorry that item is not on the menu.")

                
            # Alright I already handled the lowercase characters, but not handeling splitted characters
        if order in menu:
            total_price += menu[order]
            print(f"{order.capitalize()} added to the order. Total price: ${total_price:.2f}")
        else:
            print("Sorry, that item is not on the menu. Please choose again.")
place_order(menu)
