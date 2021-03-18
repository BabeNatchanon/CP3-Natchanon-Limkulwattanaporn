usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput  == "sexylady"  and passwordInput == "pqrs":
    print("Done !")
    print("----- iShop -----")
    print('Item list\n')
    print('1. pizza\t\t50 THB\n'
    '2. spaghetti\t\t120 THB\n'
    '3. water\t\t10 THB')
    print("-----------------")
    total = 0
    piz = int(input('How many pizza do you want?: '))
    pizPrice = 50 * piz
    total += pizPrice
    spa = int(input('How many spaghetti do you want?: '))
    spaPrice = 120 * spa
    total += spaPrice
    wat = int(input('How many bottle of water do you want?: '))
    watPrice = 10 * wat
    total += watPrice
    print()
    print('----- item summary -----')
    print()
    if piz > 0:
        print('pizza\t', 'x', piz, '\t', pizPrice)
    if spa > 0:
        print('spaghetti\t', 'x', spa, '\t', spaPrice)
    if wat > 0:
        print('water\t', 'x', piz, '\t', watPrice)
    print('Total:', total)
    print('Thank you')
else:
    print('Username or Password incorrect')