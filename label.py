import time
import asyncio
import random
from tkinter import *

root = Tk()
root.title("DVD")
root.configure(background="black")
root.minsize(400, 240)
# root.maxsize(400, 240)
root.geometry("300x300+50+50")

# Create Label in our window
image = PhotoImage(file="/Users/jamescady/Desktop/Coding_stuff/Window_Game/PythonDvD/logo.png")
image2 = image.subsample(3,3)
img = Label(root, image=image2)
img.pack()

EquX = "less"
EquY = "more"




def click():
    global EquX
    global EquY
    print("X:", root.winfo_x(), "Y:", root.winfo_y(), "  EquX:", EquX, "EquY:", EquY)
    xx = int(root.winfo_x())
    yy = int(root.winfo_y())

    if EquX == "less":
        xx -= 10
    elif EquX == "more":
        xx += 10
    
    if EquY == "less":
        yy -= 10
    elif EquY == "more":
        yy += 10

    root.geometry(f'+{xx}+{yy}')
    root.update
    bounce()
    root.after(500, click)




    

Button(text="Get position", command=click).pack()

# To top left is both negtive
# To bottom right is both postive
# To top right is x postive and y negtive
# To bottom left is x negtive and y postive

def bounce():
    global EquX
    global EquY

    if root.winfo_x() <= 0:
        print("\033[32mLEFT\033[0m")
        # Bottom left
        if EquX == "less" and EquY == "more":
            EquX = "more"
            EquY = "more"
        # Top left
        elif EquX == "less" and EquY == "less":
            EquX = "more"
            EquY = "less"


    if root.winfo_y() <= 25:
        print("\033[32mTOP\033[0m")
        # Top right
        if EquX == "more" and EquY == "less":
            EquX = "less"
            EquY = "less"
        # Top left
        elif EquX == "less" and EquY == "less":
            EquX = "less"
            EquY = "more"
        

# To top left is both negtive
# To bottom right is both postive
# To top right is x postive and y negtive
# To bottom left is x negtive and y postive


    if root.winfo_x() >= 1648:
        print("\033[32mRIGHT\033[0m")
        # Top right
        if EquX == "more" and EquY == "less":
            EquX = "less"
            EquY = "less"
        # Bottom right
        elif EquX == "more" and EquY == "more":
            EquX = "less"
            EquY = "more"


    if root.winfo_y() >= 792:
        print("\033[32mBOTTOM\033[0m")
        # Bottom right
        if EquX == "more" and EquY == "more":
            EquX = "more"
            EquY = "less"
        # Bottom left
        elif EquX == "less" and EquY == "more":
            EquX = "less"
            EquY = "less"







Button(text="Bounce?", command=bounce).pack()

root.mainloop()
