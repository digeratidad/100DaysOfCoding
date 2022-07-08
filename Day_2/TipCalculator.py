print("Welcome to Tip calculator")
amount = float(input("Enter your bill amount ($): "))
tip = float(input("What percentage of tip you want to give? 5, 10, 12 or 15?: "))
split = int(input("How many people to split the bill amount: "))
x = (amount + (0.01*tip)*amount) / split

print(f"Each person should pay: ${round(x, 2)}")
