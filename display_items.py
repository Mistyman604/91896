
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


main_food_list = [
    {"item": "Chicken Kebab", "price": 18, "stock": 25},
    {"item": "Lamb Kebab", "price": 18, "stock": 25},
    {"item": "Mixed Meat Kebab", "price": 20, "stock": 20},
    {"item": "Chicken on Chips", "price": 23, "stock": 15},
    {"item": "Lamb on Chips", "price": 23, "stock": 15},
    {"item": "Mixed Meat on Chips", "price": 25, "stock": 12},
    {"item": "Family Share Meal (Special)", "price": 50, "stock": 3},
]

food_list = []

budget = int_check("What is your budget (Minimum $18, Maximum $200)?  ", 18, 200)
print(f"Thank you for choosing your budget, we will make sure to only display items within your budget of ${budget}")

food_list = [item for item in main_food_list if item["price"] <= budget and item["stock"] > 0]

for i, item in enumerate(food_list, start=1):
    print(f"{i}. {item['item']} - ${item['price']} (Stock: {item['stock']})")


shopping_cart = []
