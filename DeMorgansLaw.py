#Asks the user for their values
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))


#Saves the valuee of expressions
va = a < b < c
vb = not (a > b or b > c)
vc = a <= b and b <= c

#prints expression values for user
print("a < b < c :", va)
print("not (a > b or b > c) :", vb)
print("a <= b and b <= c :", vc)


#tells user if it confirms De Morgans law
if vb==vc:
        print ("De Morgan's conrifmed: Expressions 2 and 3 match")
else:
        print ("De Morgan's not confirmed: Expressions 2 and 3 do not match")
