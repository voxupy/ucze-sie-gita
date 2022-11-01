print("Welcome")

size = input("What pizza u want? S, M or L?")
add_pepperoni = input("Pepperoni Y or N?")
cheese = input("Extrea cheese Y or N?")

price = 0

if size == 'S':
    price = 15
elif size == 'M':
    price = 20
else:
    price = 25

if add_pepperoni == "Y":
    price += 2

if cheese == 'Y':
    price += 3


print(f"The final price is {price}")