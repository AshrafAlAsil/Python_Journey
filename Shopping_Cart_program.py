#shopping cart program

item = input("Enter the name of the item: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity: "))
total_cost = price * quantity
print(f"You have added {quantity} of {item} to your cart. The total cost is ${total_cost:.2f}.")
# End of the shopping cart program