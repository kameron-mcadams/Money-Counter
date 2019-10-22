pennies = int(input("How many nickels do you have?"))
nickels = int(input("How many nickels do you have?"))
dimes = int(input("How many dimes do you have?"))
quarters = int(input("How many quarters do you have?"))
halfDollars = int(input("How many half dollars do you have?"))
dollars = int(input("How many dollars do you have?"))
numPennies = pennies * 1
numNickels = nickels * 5
numDimes = dimes * 10
numQuarters = quarters * 25
numHalfDollars = halfDollars * 50
numDollars = dollars * 100
total = numPennies + numNickels + numDimes + numQuarters + numHalfDollars + numDollars
money = total / 100
print("You have $" ,money, ".")
