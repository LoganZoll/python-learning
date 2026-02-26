#asks user for temperature and if its raining
temp = int(input("What's the temperature: "))
raining = input("Is it raining? Yes/No: ")

#Makes raining a bool for me
if (raining == "Yes"):
    raining = True

#Tells the user a weathor advisory message, based on weather
if(temp>100):
    print("EXTREME HEAT WARNING: Stay indoors!")
elif(temp>85 and raining):
    print("Warm rain - watch for flash floods.")
elif(temp>85):
    print("Hot and dry - stay hydrated.")
elif(temp>59 and raining):
    print("Grab an umbrella!")
elif(temp>59):
    print("Nice weather - enjoy your day!")
elif(temp>32):
    print("It's cold bundle up!.")
else:
    print("FREEZE WARNING: Roads may be icy!")
