#IMPORT THE RANDOM MODULE FOR ATM
import random
#ENDIMPORT

#AGE
def age():
    print("---------Age---------")
    name = input("Whats your name?: ")
    birthm = input("Whats your birthmonth?: ")
    birthd = input("Whats youe birthday?: ")
    birthy = int(input("Whats your birthyear?: "))
    age = 2021 - birthy
    print(f"Your name is {name}. And your birthday is {birthm} {birthd}, {birthy}")
    print(f"You are {age} years old this year.")
    #RETURN
    print("---------------------")
    rback = input("Return to menu?(y/n): ").upper()
    if rback == 'Y':
        menu()
    else:
        age()
#END AGE

#CALCULATOR
def cal():
    print("---------CALCULATOR---------")
    f_num = float(input("Input first number: "))
    op = input("Input Operator: ")
    s_num = float(input("Input second number: "))

    #YEET
    if op == '+':
        print("The answer is ", f_num + s_num)
        print("----------------------------")
    elif op == '*' or op == 'x':
        print("The answer is", f_num * s_num)
        print("----------------------------")
    elif op == '-':
        print("The answer is", f_num - s_num)
        print("----------------------------")
    elif op == '/':
        print("The answer is", f_num / s_num)
        print("----------------------------")
    
    ask = input("Return to menu?(y/n): ").upper()

    if ask == 'Y':
        menu()
    else:
        cal()
#END CALCULATOR

#GRADE
def grade():
    print("---------GRADESYSTEM---------")
    sub1 = int(input("Input your grade in Filipino: "))
    sub2 = int(input("Input your grade in English: "))
    sub3 = int(input("Input your grade in Science: "))
    sub4 = int(input("Input your grade in Math: "))
    gradecal = (sub1 + sub2 + sub3 + sub4) / 4

    if gradecal >= 93 and gradecal <= 100:
        print("You Passed")
        print("Your Average grade is 1.00")
        print("-----------------------------")
    elif gradecal >= 90 and gradecal <= 92:
        print("You Passed")
        print("Your Average grade is 1.25")
        print("-----------------------------")
    elif gradecal >= 87 and gradecal <= 89:
        print("You Passed")
        print("Your Average grade is 1.50")
        print("-----------------------------")
    elif gradecal >= 84 and gradecal <= 86:
        print("You Passed")
        print("Your Average grade is 1.75")
        print("-----------------------------")
    elif gradecal >= 80 and gradecal <= 83:
        print("You Passed")
        print("Your Average grade is 2.00")
        print("-----------------------------")
    elif gradecal >= 75 and gradecal <= 79:
        print("You Passed")
        print("Your Average grade is 2.25")
        print("-----------------------------")
    elif gradecal >= 70 and gradecal <= 74:
        print("You Passed")
        print("Your Average grade is 2.50")
        print("-----------------------------")
    elif gradecal >= 65 and gradecal <= 69:
        print("You Passed")
        print("Your Average grade is 2.75")
        print("-----------------------------")
    elif gradecal >= 60 and gradecal <= 64:
        print("You Passed")
        print("Your Average grade is 3.00")
        print("-----------------------------")
    elif gradecal >= 54 and gradecal <= 59:
        print("You Failed")
        print("Your Average grade is 4.00")
        print("-----------------------------")
    elif gradecal >= 53:
        print("You Failed")
        print("Your Average grade is 5.00")
        print("-----------------------------")

    ask = input("Return to menu?(y/n): ").upper()
    if ask == 'Y':
        menu()
    else:
        grade()
#END GRADE

#ORDER
def order():
    print("---------EATSILOG---------")
    print("[1]TAPSILOG -----PHP 75")
    print("[2]PORKSILOG -----PHP 75")
    print("[3]TOSILOG -----PHP 65")
    print("[4]CHICKSILOG -----PHP 75")
    print("[5]HOTSILOG -----PHP 60")
    print("--------------------------")
    
    order = int(input("Enter the number of your order: "))
    drinks = input("Do you want a drink(y/n): ").upper()
    if drinks == 'Y':
        print("[1]COKE -----PHP 15")
        print("[2]SPRITE -----PHP 15")
        print("[3]ICEDTEA -----PHP 15")
        print("[4]WATER -----PHP FREE")
        
        drnk = 15
        drname = " "
        
        drinkask = int(input("Enter the number of your drink: "))
        if drinkask == 1:
            drname = "COKE"
        elif drinkask == 2:
            drname = "SPRITE"
        elif drinkask == 3:
            drname = "ICEDTEA"
        else:
            drname = "WATER"

        confirmdrink = True
        
    else:
        confirmdrink = False
    
    money = int(input("Enter your money: "))
    
    if order == 1:
        name = "TAPSILOG"
        price = 75
    elif order == 2:
        name = "PORKSILOG"
        price = 75
    elif order == 3:
        name = "TOSILOG"
        price = 65
    elif order == 4:
        name = "CHICKSILOG"
        price = 75
    else:
        name = "HOTSILOG"
        price = 60
    
    if confirmdrink:
        if drinkask == 4:
            drnk = 0
            finalvalue = money - (price + drnk)
        else:
            finalvalue = money - (price + drnk)
    else:
        finalvalue = money - (price)
    

    
    fask = input("[D]ine in or [T]ake out: ").upper()
    if fask == 'D' and confirmdrink == True:
        print("**************************")
        print(f"Your order is {name} and {drname}")
        print("Your change", "PHP", finalvalue)
        print("Have a nice meal.")
        print("**************************")
    if fask == 'D' and confirmdrink == False:
        print("**************************")
        print(f"Your order is {name}")
        print("Your change", "PHP", finalvalue)
        print("Have a nice meal.")
        print("**************************")
    if fask == 'T' and confirmdrink == True:
        print("**************************")
        print(f"You order is {name} and {drname}")
        print("Your change", "PHP", finalvalue)
        print("Thanks for coming.")
        print("**************************")
    if fask == 'T' and confirmdrink == False:
        print("**************************")
        print(f"You order is {name}")
        print("Your change", "PHP", finalvalue)
        print("Thanks for coming.")
        print("**************************")
    
    ask = input("Return to menu?(y/n): ").upper()
    if ask == 'Y':
        menu()
    else:
        order()
#END ORDER

#ATM
def atm():
    money = random.randint(500, 10000)
    print("---------ATM---------")

    running = True
    
    while running:
        print("[1]-----BALANCE-----")
        print("[2]-----DEPOSIT-----")
        print("[3]-----WITHDRAW----")
        print("[4]-------EXIT------")
        ask = int(input("Enter the number of your transaction: "))

        if ask == 1:
            print("---------------------")
            print(f"Your balance is {money}")
            print("---------------------")
            ask = input("Return to menu?(y/n): ").upper()
            if ask == 'Y':
                running = True
            else:
                running = False
        elif ask == 2:
            print("---------------------")
            dpst = int(input("Enter the amount you want to deposit: "))
            moneydpst = money + dpst
            print("Transaction Sucess")
            print(f"Your balance now is {moneydpst}")
            print("---------------------")
            ask = input("Return to menu?(y/n): ").upper()
            if ask == 'Y':
                running = True
            else:
                running = False
        elif ask == 3:
            print("---------------------")
            wthdrw = int(input("Enter the amount you want to withdraw: "))
            isnotvalid = wthdrw > money

            #ERRORECHECKER
            while isnotvalid:
                wthdrw = int(input("Fix the amount you want to withdraw: "))
                whtdrw = int(wthdrw)
                isnotvalid = wthdrw > money
            #ERRORCHECKEREND

            moneywthdrw = money - wthdrw
            print("Transaction Sucess")
            print(f"Your balance now is {moneywthdrw}")
            print("---------------------")
            ask = input("Return to menu?(y/n): ").upper()
            if ask == 'Y':
                menu()
            else:
                atm()
        elif ask == 4:
            running = False
            menu()
#ENDATM

#SORT
def sorting():
    print("---------SORT---------")
    askinput = input("Enter a word:").split()
    askinput.sort()

    print("The input sorted to A-Z")
    for Everyword in askinput:
        print(askinput)
    
    print("----------------------")
    ask = input("Return to menu?(y/n): ").upper()
    if ask == 'Y':
        menu()
    else:
        sorting()
#ENDSORT

def menu():
    print("[1]Age")
    print("[2]Calculator")
    print("[3]Grading System")
    print("[4]Order")
    print("[5]ATM")
    print("[6]Sort")

    ask = int(input("Choose number: "))

    if ask == 1:
        age()
    elif ask == 2:
        cal()
    elif ask == 3:
        grade()
    elif ask == 4:
        order()
    elif ask == 5:
        atm()
    elif ask == 6:
        sorting()


#INIT THE MENU FUNCTION
menu()