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

Button(text="Get position", command=click).pack()

def click2():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    print({screen_width}, {screen_height})
    

Button(text="Screen size", command=click2).pack()

# To top left is both negtive
# To bottom right is both postive
# To top right is x postive and y negtive
# To bottom left is y postive and x negtive



def bounce():
    if root.winfo_x() == 0:
        print("\033[32mLEFT\033[0m")

    if root.winfo_y() == 25:
        print("\033[32mTOP\033[0m")

    if root.winfo_x() == 1648:
        print("\033[32mRIGHT\033[0m")

    if root.winfo_y() == 772:
        print("\033[32mBOTTOM\033[0m")

Button(text="Bounce?", command=bounce).pack()

root.mainloop()
