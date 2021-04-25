from tkinter import *

def leftClickButton(event):
    x = float(textBoxWeight.get()) / (float(textBoxHeight.get())/100)**2
    if x >= 30:
        output = "อ้วนมาก"
    elif x >= 25:
        output = "อ้วน"
    elif x >= 23:
        output = "น้ำหนักเกิน"
    elif x >= 18.6:
        output = "น้ำหนักปกติ"
    else:
        output = "ผอมเกินไป"
    result = "{} ({})".format(x, output)
    labelResult.configure(text = result)

main = Tk()
labelHeight = Label(main, text = "ส่วนสูง")
labelHeight.grid(row = 0, column = 0)
textBoxHeight = Entry(main)
labelUnit = Label(main, text = "เซนติเมตร").grid(row = 0, column = 2)
textBoxHeight.grid(row = 0, column = 1)

labelWeight = Label(main, text = "น้ำหนัก")
labelWeight.grid(row = 1, column = 0)
textBoxWeight = Entry(main)
labelUnit2 = Label(main, text = "กิโลกรัม").grid(row = 1, column = 2)
textBoxWeight.grid(row = 1, column = 1)

calculateButton = Button(main, text = "คำนวณ")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row = 2, column = 0)

labelResult = Label(main, text = "ผลลัพธ์")
labelResult.grid(row = 2, column = 1)

main.mainloop()