import random
# def print_menu():
    # print ("Character Selection")
    # print ("1. Barbarian")
    # print ("2. Bard")
    # print ("3. Cleric")
    # print ("4. Druid")
    # print ("5. Fighter")
    # print ("6. Monk")
    # print ("7. Paladin")
    # print ("8. Ranger")
    # print ("9. Rouge")
    # print ("10. Sorcerer")
    # print ("11. Warlock")
    # print ("12. Wizard")
    # print ("13. Exit")
    
# loop=True      

# while loop:          ## While loop which will keep going until loop = False
    # print_menu()    ## Displays menu

    # choice = input("Enter your choice [1-13]: ")
     
    # if choice==1:     
        # print ("Menu 1 has been selected")
        # ## You can add your code or functions here
    # elif choice==2:
        # print ("Menu 2 has been selected")
        # ## You can add your code or functions here
    # elif choice==3:
        # print ("Menu 3 has been selected")
        # ## You can add your code or functions here
    # elif choice==4:
        # print ("Menu 4 has been selected")
        # ## You can add your code or functions here
    # elif choice==5:
        # print ("Menu 5 has been selected")
        # ## You can add your code or functions here
        # loop=False # This will make the while loop to end as not value of loop is set to False
    # elif choice==6:
        # print ("Menu 6 has been selected")
        # ## You can add your code or functions here
        # loop=False # This will make the while loop to end as not value of loop is set to False
    # elif choice==7:
        # print ("Menu 7 has been selected")
        # ## You can add your code or functions here
        # loop=False # This will make the while loop to end as not value of loop is set to False
    # elif choice==8:
        # print ("Menu 8 has been selected")
        # ## You can add your code or functions here
        # loop=False # This will make the while loop to end as not value of loop is set to False
    # elif choice==9:
        # print ("Menu 9 has been selected")
        # ## You can add your code or functions here
        # loop=False # This will make the while loop to end as not value of loop is set to False
    # elif choice==10:
        # print ("Menu 10 has been selected")
        # ## You can add your code or functions here
        # loop=False # This will make the while loop to end as not value of loop is set to False
    # elif choice==11:
        # print ("Menu 11 has been selected")
        # ## You can add your code or functions here
        # loop=False # This will make the while loop to end as not value of loop is set to False
    # elif choice==12:
        # print ("Menu 12 has been selected")
        # ## You can add your code or functions here
        # loop=False # This will make the while loop to end as not value of loop is set to False
    # elif choice==13:
        # exit()
        # ## You can add your code or functions here
    # else:
        # # Any integer inputs other than values 1-5 we print an error message
        # print("Wrong option selection. Enter any key to try again..")
    

def name(nameList):
    return random.choice(nameList)

## Combines first name and last name 
def fullname(first,last):
    return '{} {}'.format(first,last)

# List of first and last names --- You done messed up A-A-RON! 
first = ['Jacqueline','Blake','Denise','Aaron','Timothy']
last = ['Smith','Doe','Miller','Brown','Sanchez']

## Prints the fullname function with the name function as it's argument with the first and last name list as it's argument

print(fullname(name(first),name(last)))   # uncomment when running

