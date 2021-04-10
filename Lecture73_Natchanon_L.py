systemeMenu = {"pizza": 30 , "burger": 20 , "water": 5}
menuList = []

def showBill():
    total = 0
    print(" ----My Food ----")
    for number in range(len(menuList)):
        total += menuList[number][1]
        print(menuList[number][0] , menuList[number][1])
        print("Total: " , total)

while True:
    menuName = input("Please Enter menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuList.append([menuName , systemeMenu[menuName]])

print(menuList)
showBill()