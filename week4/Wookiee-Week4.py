#print("Fuck you Keegan")
#Daryn = "Big Poppa"
#print("Hey " + Daryn + " I Love You!")
#print(f'Hey {Daryn} {69 * 420}')

CalcFunctions = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Division"]
CalcSymbols = ["+", "-", "*", "/"]
n1 = input("Please enter your first Number")

print("Please choose a function")
print(*CalcFunctions, sep = "\n")
Method = input()

if Method == "1":
    print("Addition")
elif Method == "2":
    print("Subtraction")
elif Method == "3":
    print("Multiplication")
else:
    print("Division")

n2 = input("Please enter your second Number")

if Method == "1":
    solve = int(n1) + int(n2)
elif Method == "2":
    solve = int(n1) - int(n2)
elif Method == "3":
    solve = int(n1) * int(n2)
else:
    solve = int(n1) / int(n2)

print(n1, CalcSymbols[int(Method) - 1], n2)
print("Your answer is:")
print(solve)