#Written by Shiven Desai
class RetailItem:
    def __init__(self, description, units_in_inventory, price):
        self.description = description
        self.units_in_inventory = units_in_inventory
        self.price = price

# create three RetailItem objects with the given data
item1 = RetailItem("Jacket", 12, 59.95)
item2 = RetailItem("Designer Jeans", 40, 34.95)
item3 = RetailItem("Shirt", 20, 24.95)

# display the data for each item on the screen
print("Item #1:")
print("Description:", item1.description)
print("Units in Inventory:", item1.units_in_inventory)
print("Price: $", format(item1.price, ".2f"), sep="")

print("\nItem #2:")
print("Description:", item2.description)
print("Units in Inventory:", item2.units_in_inventory)
print("Price: $", format(item2.price, ".2f"), sep="")

print("\nItem #3:")
print("Description:", item3.description)
print("Units in Inventory:", item3.units_in_inventory)
print("Price: $", format(item3.price, ".2f"), sep="")
