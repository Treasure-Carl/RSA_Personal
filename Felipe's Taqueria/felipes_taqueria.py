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




















# users_input = input("Enter a key (case insensitive): ")
# users_input_lower = users_input.lower()
# # print(users_input_lower)

# # looping through the dictionary with the case insensitive key
# for key in menu:
#     if key.lower() == users_input_lower:
#         print(f"key: {key} - value: {menu[key]}\n")
#         # break
# while True:
#     new_list = 0.0
#     new_list  += menu[key]
#     print(new_list)
    
# # values = menu.values()
# # items = menu.items()

# # get(), clear()

# # looping through dictionaries
# # for keys in menu:
# #     print(keys)

# # for values in menu.values():
# #     print(values)

# # for key, value in menu.items():
# #     print(key, value, end=": ")

# # answer = input("")

# # users_input = input("Enter a key (case insensitive): ")
# # users_input_lower = users_input.lower()
# # print(users_input_lower)

