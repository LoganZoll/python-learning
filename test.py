
added_toppings = []

user_input = input("Enter topping number. Type done to finish ")
print(user_input)
while user_input != "done":
    if user_input.isdigit() and int(user_input)>0 and int(user_input)<9:
        added_toppings.append(user_input)
    else:
        print("Not a topping")
    user_input = input("Enter topping number. Type done to finish ")


