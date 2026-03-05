#Distance converter

#Gets users input
current_unit = input("What unit of measurement do you currently have mi/km: ").lower()
current_value = float(input("What distance value do you need converted: "))


#Converts miles to kilometers
if current_unit=="mi":
    new_value = current_value*1.60934
    print(f"Your distance in kilometers: {new_value:.2f}")
#Converts kilometers to miles
elif current_unit=="km":
    new_value = current_value*0.621371
    print(f"Your distance in miles: {new_value:.2f}")
#Checks if the input is invalid
else:
    print("Invalid unit.")