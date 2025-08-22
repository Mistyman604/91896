print(make_statement("🛒 Checkout Summary", "🛒"))


# ---- Receipt Generation ----
# create dataframe / table from dictionary
receipt = pandas.DataFrame(cart)

# Currency Formatting (uses currency function)
receipt["Total"] = receipt["price"] * receipt["quantity"]
for column in ["price", "Total"]:
    receipt[column] = receipt[column].apply(currency)

# Output receipt frame without index
receipt_string = receipt.to_string(index=False)

# Additional strings / Headings
heading_string = make_statement("Car Purchase Receipt", "=")
summary_heading = make_statement("Summary", "-")

# Total calculations
total_cost = sum(item["price"] * item["quantity"] for item in cart)
summary = [
    f"Total Cost: {currency(total_cost)}"
]

# List of strings to be outputted / written to file
to_write = [heading_string, "\n",
            name + "'s Receipt", "\n",
            summary_heading,
            receipt_string, "\n",
            *summary]


# Print area
print()
for item in to_write:
    print(item)

# create file to hold data (add .txt extension)
file_name = "car_purchase_receipt"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

# write the item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")

text_file.close()