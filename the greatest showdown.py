#task 1 identify the greatest
print("i can identify the greatest and smallest\n")

name = input("so what is your name\n")
 
number1 =float(input(f"give and a number {name}?!\n"))
number2 =float(input(f"now a second number {name}?!\n"))
number3 =float(input(f"now a third number {name}?!\n"))


if number1 > number2 and number1 >number3:
    print(f"the greatest number is {number1}, {name}!")
elif number2 > number1 and number2 >number3:
    print(f"the greatest number is {number2}, {name}!")
else:
    print(f"the greatest number is {number3}, {name}!")





#task 2 identify the greatest and the smallest
print("i can identify the greatest and smallest\n")

name = input("so what is your name\n")
 
number1 =float(input(f"give and a number {name}?!\n"))
number2 =float(input(f"now a second number {name}?!\n"))
number3 =float(input(f"now a third number {name}?!\n"))


if number1 > number2 and number1 >number3:
    print(f"the greatest number is {number1}, {name}!")
elif number2 > number1 and number2 >number3:
    print(f"the greatest number is {number2}, {name}!")
else:
    print(f"the greatest number is {number3}, {name}!")
    

# Identify the smallest number
if number1 < number2 and number1 < number3:
    print(f"The smallest number is {number1}, {name}!")
elif number2 < number1 and number2 < number3:
    print(f"The smallest number is {number2}, {name}!")
else:
    print(f"The smallest number is {number3}, {name}!")    