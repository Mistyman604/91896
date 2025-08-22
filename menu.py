# Importing packages
import pandas

import numpy as np

# Creating menu
all_order_options = ["Chicken Kebab", "Lamb Kebab", "Mixed Meat Kebab", "Chicken On Chips", "Lamb On Chips",
                     "Mixed Meat On Chips", "Family Share Meal"]
all_order_price = [18,18,20,23,23,25, 50]

order_dict = {
    'Orders': all_order_options,
    'Price ($)': all_order_price,
}

# create dataframe / table from dictionary
order_frame = pandas.DataFrame(order_dict)

# Rearranging index
order_frame.index = np.arange(1, len(order_frame) + 1)

print("Order")
print(order_frame)
print()