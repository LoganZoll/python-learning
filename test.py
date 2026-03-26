# ============================================
# PIZZA ORDER SYSTEM
# CS 1300 — Lecture 6 Lab
# ============================================
# ----- Menu Data (do not modify) -----
sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
size_prices = [6.99, 9.99, 12.99, 16.99]
topping_names = ["Pepperoni", "Mushrooms", "Green Peppers", "Onions",
"Sausage", "Bacon", "Extra Cheese", "Pineapple"]
topping_price = 1.50 # each topping, any size
order_descriptions = [] # e.g., "Large Pepperoni, Mushrooms"
order_prices = [] # e.g., 15.99

#Border
print ("="*30)
print ("\tPIZZA SIZES")
print ("="*30)


#Loops through and prints the sizes and their price
for i in range(len(sizes)):
    print(f"{i+1}. {sizes[i]}  \t{size_prices[i]:>5}")
#Border
print ("="*30)
