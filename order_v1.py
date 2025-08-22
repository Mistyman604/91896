# Importing packages
import pandas

import numpy as np

# Creating menu
all_sauce_options = ["Tomato", "Yoghurt", "Mayonnaise", "Mint sauce", "Garlic",
                     "BBQ", "Sweet Chilli", "Aioli"]
all_sauce_price = [0.50, 1.50, 1.50, 1.00, 0.50, 0.50, 0.50, 0.50]

sauce_dict = {
    'Sauces': all_sauce_options,
    'Price ($)': all_sauce_price,
}

# create dataframe / table from dictionary
sauce_frame = pandas.DataFrame(sauce_dict)

# Rearranging index
sauce_frame.index = np.arange(1, len(sauce_frame) + 1)

print("SAUCES")
print(sauce_frame)
print()