# ============================================
# PIZZA ORDER SYSTEM
# CS 1300 — Lecture 6 Lab
# ============================================

# ----- Menu Data (do not modify) -----
sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
size_prices = [6.99, 9.99, 12.99, 16.99]
topping_names = ["Pepperoni", "Mushrooms", "Green Peppers", "Onions", "Sausage", "Bacon", "Extra Cheese", "Pineapple"]
topping_price = 1.50  # each topping, any size


# ----- Order Storage -----
order_descriptions = []  # e.g., "Large Pepperoni, Mushrooms"
order_prices = []        # e.g., 15.99


# Main Ordering System
while True:
    print("="*30)
    print("\tPIZZA SIZES")
    print("="*30)
    
    for i in range(len(sizes)):
        print(f"{i+1}. {sizes[i]}  \t{size_prices[i]:>5}")
    print("="*30)
    
    # Ask for pizza size
    try:
        size_choice = int(input("Pick a size (1-4): "))
        if size_choice < 1 or size_choice > 4:
            print("Choose 1-4.")
            continue
    except ValueError:
        print("Please enter a number!")
        continue
    
    # Show toppings
    print("\nTOPPINGS:")
    for i in range(len(topping_names)):
        print(f"{i+1}. {topping_names[i]}")

    # Select toppings
    selected_toppings = []
    user_input = input("Enter Topping Number. Type done to finish: ")

    while user_input.lower() != "done":
        if user_input.isdigit() and 1 <= int(user_input) <= 8:
            topping = topping_names[int(user_input) - 1]
            # Adds the toppings to the selected toppings
            if topping not in selected_toppings:
                selected_toppings.append(topping)
                print(f"Added {topping}.")
            else:
                print("Already added!") # Makes sure there isn't any dupilcates
        else:
            print("Not a Topping")
        user_input = input("Enter topping number. Type done to finish: ")


    # Calculate price
    price = size_prices[size_choice - 1] + len(selected_toppings) * topping_price
    
    # Store pizza
    order_descriptions.append(f"{sizes[size_choice - 1]} - {', '.join(selected_toppings)}")
    order_prices.append(price)
    
    print(f"Added pizza: {order_descriptions[-1]} - ${price:.2f}")

    # Ask if they want another pizza
    pizza = True
    while pizza:     
        order_another = input("Order another pizza? (y/n): ").lower()
        if order_another=="y":
            pizza = False
            continue
        if order_another=="n":
            break
        else:
            print("That wasn't an option")

subtotal = sum(order_prices)
tax = sum(order_prices) * 0.07


print("="*35)
print("\tYOUR ORDER RECEIPT")
print("="*35)
for i in range(len(order_descriptions)):
    print(f"{i+1}. {order_descriptions[i]} \n          {order_prices[i]}")
print("="*35)
print(f"Subtotal:                     ${subtotal:.2f}")
print(f"Tax (7%):                     ${tax:.2f}")
print(f"Total:                        ${sum(order_prices) + tax:.2f}")
print("="*35)








for i in range(len(size
























personal_count=0
medium_count=0
large_count=0
party_count=0

for i in range(len(order_descriptions)):
    print (order_descriptions[i][0:5])
    if order_descriptions[i][0:5]=="Large":
        large_count +=1
    if order_descriptions[i][0:5]=="Perso":
        personal_count+=1
    if order_descriptions[i][0:5]=="Mediu":
        medium_count+=1
    if order_descriptions[i][0:5]=="Party":
        party_count+=1

print(f"personal count {personal_count}, medium count {medium_count}, large count {large_count}, party count {party_count}")  
