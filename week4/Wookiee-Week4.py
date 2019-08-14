#print("Fuck you Keegan")
#Daryn = "Big Poppa"
#print("Hey " + Daryn + " I Love You!")
#print(f'Hey {Daryn} {69 * 420}')

CalcFunctions = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Division", "5. Squared", "6. Cubed"]
CalcSymbols = ["+", "-", "*", "/", "²", "³"]

def ask1():
    global n1
    n1 = input("Please enter a whole number.")
    if not n1.isdigit():
        return ask1()

def ask2():
    global Method
    print("Please choose a function by entering the corresponding number.")
    print(*CalcFunctions, sep = "\n")
    Method = input()
    if not Method.isdigit():
        return ask2()

def ask3():
    global n2
    n2 = input("Please enter a second whole number.")
    if not n2.isdigit():
        return ask3()

ask1()
ask2()

if Method == "5":
    solve = int(n1) ** 2
    print(n1, CalcSymbols[int(Method) - 1])
    print("Your answer is:")
    print(solve)
    quit()
if Method == "6":
    solve = int(n1) ** 3
    print(n1, CalcSymbols[int(Method) - 1])
    print("Your answer is:")
    print(solve)
    quit()

ask3()

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