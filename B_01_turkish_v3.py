# Import
import pandas

import numpy as np

import random


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

        print(f"Please say either yes or no Bossman")


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


def int_check(question, min, max):
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


def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)


# Lists

main_food_list = [
    {"item": "Chicken Kebab", "price": 12, "stock": 25},
    {"item": "Lamb Kebab", "price": 12, "stock": 25},
    {"item": "Mixed Meat Kebab", "price": 16, "stock": 20},
    {"item": "Chicken on Chips", "price": 20, "stock": 15},
    {"item": "Lamb on Chips", "price": 20, "stock": 15},
    {"item": "Mixed Meat on Chips", "price": 25, "stock": 12},
    {"item": "Family Share Meal (Special)", "price": 50, "stock": 3},
]

food_list = []

# Ask for a Budget
print("Let's establish a budget for you Bossman")
budget = int_check("What is your budget (Minimum $18, Maximum $200)?\n", 18, 200)
print(f"Thank you for choosing your budget, we will make sure to only display items within your budget of ${budget}\n")

# Creating list of food they can buy
food_list = [item for item in main_food_list if item["price"] <= budget and item["stock"] > 0]

# Displaying that list
for i, item in enumerate(food_list, start=1):
    print(f"{i}. {item['item']} - ${item['price']} (Stock: {item['stock']})")

want_food = int_check("Please select the number of which food you would like?", 1, 7)
selected_item = food_list[want_food-1]
print(f"You selected: {selected_item['item']} price: {selected_item['price']}")
budget = budget - selected_item['price']
print(f"Your new budget is {budget}")






# Payment and Delivery


# End of Ticket Loop!
