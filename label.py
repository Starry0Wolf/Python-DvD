import time
import asyncio
import random
from tkinter import *

root = Tk()
root.title("DVD")
root.configure(background="black")
root.minsize(400, 240)
root.maxsize(400, 240)
root.geometry("300x300+50+50")

# Create Label in our window
image = PhotoImage(file="/Users/jamescady/Desktop/Coding_stuff/Window_Game/PythonDvD/logo.png")


# logo1 = PhotoImage(file="/Users/jamescady/Desktop/Coding_stuff/Window_Game/PythonDvD/Logos1/dvdlogo-01.png").subsample(3,3)
# logo2 = PhotoImage(file="/Users/jamescady/Desktop/Coding_stuff/Window_Game/PythonDvD/Logos1/dvdlogo-02.png").subsample(3,3)
# logo3 = PhotoImage(file="/Users/jamescady/Desktop/Coding_stuff/Window_Game/PythonDvD/Logos1/dvdlogo-03.png").subsample(3,3)
# logo4 = PhotoImage(file="/Users/jamescady/Desktop/Coding_stuff/Window_Game/PythonDvD/Logos1/dvdlogo-04.png").subsample(3,3)
# logo5 = PhotoImage(file="/Users/jamescady/Desktop/Coding_stuff/Window_Game/PythonDvD/Logos1/dvdlogo-05.png").subsample(3,3)
# logo6 = PhotoImage(file="/Users/jamescady/Desktop/Coding_stuff/Window_Game/PythonDvD/Logos1/dvdlogo-06.png").subsample(3,3)
# logo7 = PhotoImage(file="/Users/jamescady/Desktop/Coding_stuff/Window_Game/PythonDvD/Logos1/dvdlogo-07.png").subsample(3,3)


# logo_num = 0

# def switch():
    # global logo_num
    # global logo
    # global logo1
    # global logo2
    # global logo3
    # global logo4
    # global logo5
    # global logo6
    # global logo7
    # # global image
    # logo_num += 1
    # if logo_num >= 8:
    #     logo_num = 1


    # if logo_num == 1:
    #     logo = logo1
    # elif logo_num == 2:
    #     logo = logo2
    # elif logo_num == 3:
    #     logo = logo3
    # elif logo_num == 4:
    #     logo = logo4
    # elif logo_num == 5:
    #     logo = logo5
    # elif logo_num == 6:
    #     logo = logo6
    # elif logo_num == 7:
    #     logo = logo7
 


    

#     print(logo_num)
#     logo = image
#     # image = image.subsample(3,3)
#     img = Label(root, image=image)
#     img.pack()



# switch()


image = image.subsample(3,3)
img = Label(root, image=image)
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
    root.after(50, click)




    

# Button(text="Get position", command=click).pack()

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
            # switch()
        # Top left
        elif EquX == "less" and EquY == "less":
            EquX = "more"
            EquY = "less"
            # switch()


    if root.winfo_y() <= 25:
        print("\033[32mTOP\033[0m")
        # Top right
        if EquX == "more" and EquY == "less":
            EquX = "less"
            EquY = "less"
            # switch()
        # Top left
        elif EquX == "less" and EquY == "less":
            EquX = "less"
            EquY = "more"
            # switch()
        

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
            # switch()
        # Bottom right
        elif EquX == "more" and EquY == "more":
            EquX = "less"
            EquY = "more"
            # switch()


    if root.winfo_y() >= 792:
        print("\033[32mBOTTOM\033[0m")
        # Bottom right
        if EquX == "more" and EquY == "more":
            EquX = "more"
            EquY = "less"
            # switch()
        # Bottom left
        elif EquX == "less" and EquY == "more":
            EquX = "less"
            EquY = "less"
            # switch()




click()


# Button(text="Bounce?", command=bounce).pack()
# Button(text="switch", command=switch).pack()

root.mainloop()