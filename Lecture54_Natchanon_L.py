def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

print('Welcome to the cashier')

count = 3

while count > 0:
    x = login()
    if x == True:
        showMenu()
        if menuSelect() == 1:
            total = int(input('Please insert total price: '))
            print(vatCalculator(total))
        elif menuSelect() == 2:
            print(priceCalculator())
    else:
        print('Please fill again')
        count -= 1

