# Import
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


def phone(question, min, max):
    error = f'Please enter a valid phone number between {min} and {max} numbers long'

    while True:

        try:

            response = input(question)

            if response.isdigit() and min <= len(response) <= max:
                return response
            elif len(response) > max:
                print("Sorry, That isn't a legal phone number")
                print(error)
            elif len(response) < min:
                print("Sorry, That isn't a legal phone number")
                print(error)
            else:
                print(error)

        except ValueError:
            print(error)


# initialise variables / non-default options for string checker
payment_ans = ('cash', "credit")
heading_string = make_statement("TERRY'S TURKISH TEMPLE", "=")
active_order = 1

# Credit card surcharge (currently 5%)
CREDIT_SURCHARGE = 0.05

while active_order == 1:

    main_food_list = [
        {"item": "Chicken Kebab", "price": 12, "stock": 25, "quantity": 0},
        {"item": "Lamb Kebab", "price": 12, "stock": 25, "quantity": 0},
        {"item": "Mixed Meat Kebab", "price": 16, "stock": 20, "quantity": 0},
        {"item": "Chicken on Chips", "price": 20, "stock": 15, "quantity": 0},
        {"item": "Lamb on Chips", "price": 20, "stock": 15, "quantity": 0},
        {"item": "Mixed Meat on Chips", "price": 25, "stock": 12, "quantity": 0},
        {"item": "Family Share Meal (Special)", "price": 50, "stock": 3, "quantity": 0},
    ]

    # print heading
    print(f"{heading_string}")

    # initialising lists, variabales...etc
    food_list = []
    cart = []
    running_price = 0

    # get the users name
    name = not_blank("What is your name?")

    # get the users phone number
    phone_number = phone("What is your phone number?    ", 8, 11)

    # ask if they want to see the instructions
    want_instructions = string_check("Do you want to see the instructions?   ")
    # display if 'yes'
    if want_instructions == "yes":
        instructions()

    # Ask for a Budget
    print("Let's establish a budget for you ")
    budget = budget_check("What is your budget (Minimum $12, Maximum $200)?\n", 12, 200)
    original_budget = budget
    print(
        f"Thank you for choosing your budget, we will make sure to only display items within your budget of ${budget}\n"
    )

    # create a loop function, so they can order food while their budget is higher than what the cheapest item is
    while budget > 11.99:
        # Creating list of food they can buy
        food_list = [item for item in main_food_list if item["price"] <= budget and item["stock"] > 0]

        # Displaying that list
        for i, item in enumerate(food_list, start=1):
            print(f"{i}. {item['item']} - ${item['price']} (Stock: {item['stock']})")
        print()

        # ask user for input on what food they would like
        want_food = int_check("Please select the number of which food you would like?", 0, 7)

        # checks to see if they inputted 0 which means they dont want anything
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
            selected_items = int_check(f"How many {selected_item['item']}'s would you like?", 0, int(max_amt))

            # else, they would only be able to buy one, hence well just add it to cart
        else:
            selected_items = 1
            print("You can only afford 1, so we’ll add that.")

        if selected_items >= 1:
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
            print(f"Your new budget is {currency(budget)}")
            print()

    # checks if budget is still equal to or higher than 12 and if it isn't, the current order ends and this message
    # displays
    if budget < 12:
        print("Whoops! It Looks like you don't have enough money to buy more food\n")
        print()

    # asks the user if they are happy with their cart and would like to continue to payment
    want_to_continue = string_check("Are you satisfied with your order and wish to continue to payment")
    print()
    if want_to_continue == 'yes':
        active_order = active_order - 1
    elif want_to_continue == 'no':
        continue

# receipt
receipt = pandas.DataFrame(cart)

# currency formatting
receipt["Total"] = receipt["price"] * receipt["quantity"]
for column in ["price", "Total"]:
    receipt[column] = receipt[column].apply(currency)

# Output receipt frame without index
receipt_string = receipt.to_string(index=False)

# strings and headings
order_details_heading = make_statement("Order Details", "-")

total_paid = sum(item['price'] * item['quantity'] for item in cart)
num_sold = sum(item['quantity'] for item in cart)
num_sold_string = f"Total items: {num_sold}"
name_string = f"Name: {name}"
phone_string = f"Phone: {phone_number}"

# ask user for payment method (cash / credit / ca / cr)
pay_method = string_check("Payment method: ", payment_ans, 2)

if pay_method == "cash":
    surcharge = 0

    # if paying by credit, calculate surcharge
else:
    surcharge = total_paid * CREDIT_SURCHARGE
    total_paid += total_paid * CREDIT_SURCHARGE

pay_method_string = f"Payment Method: {pay_method}"
total_paid_string = f"Grand Total: {currency(total_paid)}"
surcharge_string = f"Surcharge: {currency(surcharge)} (only applies to payment made with card"

# List of strings to be outputted / written to file
to_write = [heading_string,
            order_details_heading,
            name_string,
            phone_string,
            receipt_string, "\n",
            pay_method_string,
            surcharge_string,
            total_paid_string,
            num_sold_string, ]

for item in to_write:
    print(item)
# create file to hold data (add .txt extension)
file_name = "turkish_receipt"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

# write the item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
