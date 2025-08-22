import pandas

import numpy as np

import random

import math


# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at the start and end"""
    return f"{decoration * 3} {statement} {decoration * 3}"


def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    """Checks that users enter the full word or the 'n' letter/s of a word from a list of valid responses"""
    while True:
        response = input(question).lower()

        for item in valid_answers:
            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the "n" letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


def instructions():
    print(make_statement("Instructions", "ℹ️"))

    print('''
WELCOME TO TERRY'S TURKISH TEMPLE
To place your order, please follow the steps below:

- Fill Out the Order Form:

- Enter your full name

- List your order items clearly

- Select your payment method: Cash or Card

- Choose either Delivery or Pickup

- Double-check your details before submitting to avoid delays.

Thank you for choosing Terry’s Turkish Temple – where every bite is a delight! 😁
    ''')


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry this can't be blank. Please try again. \n")


def budget_check(question, min, max):
    """Checks users enter an integer"""

    error = f"Please enter a number between {min} and {max}"

    while True:

        try:

            response = int(input(question))

            if min <= response <= max:
                return response
            elif response > max:
                print("Sorry, too high a budget will cause too much stress on our employees")
                print(error)
            elif response < min:
                print("Sorry, you cant buy anything on our menu")
                print(error)
            else:
                print(error)

        except ValueError:
            print(error)


def int_check(question, min, max):
    """Checks users enter an integer"""

    error = f"Please enter a number between {min} and {max}"

    while True:

        try:

            response = int(input(question))

            if min <= response <= max:
                return response
            elif response > max:
                print(error)
            elif response < min:
                print(error)
            else:
                print(error)

        except ValueError:
            print(error)

def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)

main_food_list = [
        {"item": "Chicken Kebab", "price": 12, "stock": 25, "quantity": 0},
        {"item": "Lamb Kebab", "price": 12, "stock": 25, "quantity": 0},
        {"item": "Mixed Meat Kebab", "price": 16, "stock": 20, "quantity": 0},
        {"item": "Chicken on Chips", "price": 20, "stock": 15, "quantity": 0},
        {"item": "Lamb on Chips", "price": 20, "stock": 15, "quantity": 0},
        {"item": "Mixed Meat on Chips", "price": 25, "stock": 12, "quantity": 0},
        {"item": "Family Share Meal (Special)", "price": 50, "stock": 3, "quantity": 0},
    ]

food_list = []
cart = []
running_price = 0

print("Let's establish a budget for you ")
budget = budget_check("What is your budget (Minimum $12, Maximum $200)?\n", 12, 200)
original_budget = budget
print(
    f"Thank you for choosing your budget, we will make sure to only display items within your budget of ${budget}\n"
)

while True:
    # Creating list of food they can buy
    food_list = [item for item in main_food_list if item["price"] <= budget and item["stock"] > 0]

    # Displaying that list
    for i, item in enumerate(food_list, start=1):
        print(f"{i}. {item['item']} - ${item['price']} (Stock: {item['stock']})")
    print()

    # ask user for input on what food they would like
    want_food = int_check("Please select the number of which food you would like?", 0, 7)
    # checks to see if they inputted 0 which means they don't want anything
    if want_food == 0:
        print("You have ended your current order")
        break

    # setting the max amount of that item they can buy
    selected_item = food_list[want_food - 1]
    max_amt = int(budget / selected_item['price'])
    max_amt = math.floor(max_amt)

    # sets the max they can buy to be whatever is lower: budget minimum or stock minimum
    if max_amt > selected_item["stock"]:
        max_amt = selected_item["stock"]
    print(f"You can buy up to {max_amt} of this item")

    # asks user how many of those items they would like if they can afford more than 1
    if max_amt > 1:
        selected_items = int_check(f"How many {selected_item['item']}'s would you like?", 1, int(max_amt))

        # else, they would only be able to buy one, hence well just add it to cart
    else:
        selected_items = 1
        print("You can only afford 1, so we’ll add that.")

    # Track Totals
    selected_item['quantity'] += selected_items
    print()

    # Add to cart
    cart.append({
        "item": selected_item['item'],
        "price": selected_item['price'],
        "quantity": selected_items
    })

    # update totals
    budget -= selected_item['price'] * selected_items
    running_price += selected_item['price'] * selected_items
    selected_item['stock'] -= selected_items

    # Print Feedback
    print(f"You selected {selected_items}: {selected_item['item']} price: ${selected_item['price']}")
    print()
    print(f"You have spent a total of: {currency(running_price)} so far")
    print(f"Your new budget is {budget}")
    print()