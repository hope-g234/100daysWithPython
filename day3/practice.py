print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
ticket = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input(" But What is your age? "))
    if age <= 12:
        ticket = 5
        print("please pay $5")
    elif age <= 18:
        ticket = 7
        print("please pay $7")
    elif age >= 45 and age <= 60:
        print ("have a free ride")
    else:
        ticket = 12
        print("please pay $12")
    want_photo = input("Do you want to have a photo taken? type y for yes and n for No\n")
    if want_photo == "y":
        ticket += 3

    print(f"Your final bill is ${ticket}")
else:
    print("Sorry you have to grow taller before you can ride the rollercoaster!")



# Pizza order practice
print("Welcome to python pizza Deliveries!")
size = input("what size pizza do you want? S , M or L\n")
pepperoni = input ("Do you want Pepperoni? y or n\n")
extra_cheese = input("Do you want extra cheese? y or n\n")
bill = 0
if size == "S":
    if pepperoni == "y":
        bill = 17
    else:
        bill = 15

elif size == "M":
    if pepperoni == "y":
        bill = 23
    else:
        bill = 20
elif size == "L":
    if pepperoni == "y":
        bill = 28
    else:
        bill = 25
else:
    print("You typed wrong input")

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is ${bill}")