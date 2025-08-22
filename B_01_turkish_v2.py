import pandas
import random


# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at the start and end"""
    return f"{decoration * 3} {statement} {decoration * 3}"
5

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

    error = f"Oops - please enter an integer between {min} and {max}"

    while True:

        try:

            response = int(input(question))

            if min <= response <= max:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)


# Lists
Main_Food_List = [
    {"item": "Chicken Kebab", "price": 18, "Stock": 25},
    {"item": "Lamb Kebab", "price": 18, "Stock": 25},
    {"item": "Mixed Meat Kebab", "price": 20, "Stock": 20},
    {"item": "Chicken on Chips", "price": 23, "Stock": 15},
    {"item": "Lamb on Chips", "price": 23, "Stock": 15},
    {"item": "Mixed Meat on Chips", "price": 25, "Stock": 12},
]
# Ask for a Budget
print("BLah, lets establish a budget for you bossman")
budget = int_check("What is your budget (Minimum $18, Maximum $100)?  ", 18, 100)
print(f"Thank you for choosing your budget, we will make sure to only display items within your budget of ${budget}")
# Order Stage 1 Loop


# Order Stage 2 loop


# Payment and Delivery


# End of Ticket Loop!
