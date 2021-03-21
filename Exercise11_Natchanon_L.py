number = int(input())
for i in range(number):
    text = ''
    for j in range(3):
        if (j+1) % 2 != 0:
            text = text + (' ' * (number -(i + 1)))
        else:
            text = text + ('*' * (2 * i + 1))
    print(text)
