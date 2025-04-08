
# ------------------------------ Explanation ---------------------------------- #
# Bonus ideas:
# ------------
# - Make the cart interactive: ask the user to input items one by one in a loop.
# - Handle products not found in the price list.
# - Allow the user to type 'done' to finish the cart.
# - Display a summary of what the user ordered with a final total.
#
# Order of functions:
# You can exit at any stage by typing quit.
# 1. Import product into cart == str
# 2. Quantity == int
# 3. Data compatibility:
# 3.1 If the info does not match - error, and ask correct
# 3.2 If the info is correct - go to step 4
# 4. Ask if you want to add more products to the cart
# 4.1 If yes, return to the beginning
# 4.2 If not, output a summary

# ------------------------------ General ---------------------------------- #

import random
import re


def create_price():
    x = random.uniform(1, 10)
    return round(x, 2)


# ------------------------------ Add Items and Quantity------------------------------- #

def add_item():
    global item_to_cart
    while True:
        item_to_cart = input(
            "Add name of item to cart, to finsh, write 'done': ").lower()  # "avocado"
        if re.fullmatch('[a-zA-Z ]+', item_to_cart):
            return item_to_cart
        else:
            print("not a valid item.")


def add_quantity():
    global quantity_to_cart
    while True:
        quantity_to_cart = input("Quantity: ")  # 5
        if quantity_to_cart.isnumeric():
            quantity_to_cart = int(quantity_to_cart)
            return quantity_to_cart
        else:
            print("not a valid number.")

# ------------------------- Update cart with items ------------------------------- #


def update_cart(item_to_cart, quantity_to_cart):
    cart_items.update({item_to_cart: quantity_to_cart})
    product_prices.update({item_to_cart: create_price()})
    print(product_prices)
    print(cart_items)

# ------------------------- Calculation ------------------------------- #


def calculate_cart_total(cart_items, product_prices):
    """
    Calculates the total price of all items in the cart.

    """
    total = 0
    for product, quantity in cart_items.items():
        total += quantity * product_prices.get(product, 0)
    return round(total, 2)

# ---------------------------- DB Product ------------------------------- #


# Example product prices
product_prices = {
    "apple": 3.0,
    "banana": 2.5,
    "milk": 7.0,
    "bread": 5.0
}

# Example cart items (product: quantity)
cart_items = {
    "apple": 2,
    "banana": 5,
    "milk": 1,
    "bread": 3
}

# ------------------------------ Total ------------------------------- #

while True:
    new_item = add_item()
    print(new_item)

    if new_item == "done":
        break
    else:
        new_quantity = add_quantity()
        print(new_quantity)
        update_cart(new_item, new_quantity)

print(product_prices)
print(cart_items)
total = calculate_cart_total(cart_items, product_prices)
print(total)  # Expected: 2*3.0 + 1*7.0 + 3*5.0 = 6 + 7 + 15 = 28.0
