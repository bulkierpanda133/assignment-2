print("a leap year checker")

name = str(input("what is your name?\n"))



year = int(input(f"enter a year {name}!\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"the year {year} is a leap year {name}!!!!!!")
        else:
            print(f"the year {year} is not a leap year {name}:(")
    else:
        print(f"the year {year} is a leap year {name}!!!!.")
else:
    print(f"the year {year} is not a leap year {name}:(")        