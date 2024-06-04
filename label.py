import time
import asyncio
import random
from tkinter import *
from PIL import ImageTk, Image
import itertools

root = Tk()
root.title("DVD")
root.configure(background="black")
root.minsize(400, 240)
root.maxsize(400, 240)
root.geometry("300x300+50+50")

# Create Label in our window
# image = PhotoImage(file="/Users/jamescady/Desktop/Coding_stuff/Window_Game/PythonDVD/logo.png")

panel = Label(root)
panel.pack()
folderr22="/Users/jamescady/Desktop/Coding_stuff/Window_Game/PythonDVD/Version2/new/Cloudconvert/download-"

# file="/Users/jamescady/Desktop/Coding_stuff/Window_Game/Version2/Cloudconvert
# , 'dvdlogo-02.jpeg', 'dvdlogo-03.jpeg', 'dvdlogo-04.jpeg', 'dvdlogo-05.jpeg', 'dvdlogo-06.jpeg', 'dvdlogo-07.jpeg'
images = [folderr22 + "1.png", folderr22 + "2.png", folderr22 + "3.png", folderr22 + "4.png", folderr22 + "5.png", folderr22 + "6.png", folderr22 + "7.png"]
images = iter(images)  # make an iterator
images = itertools.cycle(images)

def next_img(timeNOW):
    try:
        img = next(images)  # get the next image from the iterator
        root.after(timeNOW, next_img)
        timeNOW = 100
        
    except StopIteration:
        return  # if there are no more images, do nothing

    # load the image and display it
    
    img = Image.open(img)
    img = ImageTk.PhotoImage(img)
    panel.img = img  # keep a reference so it's not garbage collected
    panel['image'] = img



# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# print(screen_height, screen_width)
    


# image = image.subsample(3,3)
# img = Label(root, image=image)
# img.pack()


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
            next_img(0)
        # Top left
        elif EquX == "less" and EquY == "less":
            EquX = "more"
            EquY = "less"
            next_img(0)


    if root.winfo_y() <= 25:
        print("\033[32mTOP\033[0m")
        # Top right
        if EquX == "more" and EquY == "less":
            EquX = "less"
            EquY = "less"
            next_img(0)
        # Top left
        elif EquX == "less" and EquY == "less":
            EquX = "less"
            EquY = "more"
            next_img(0)

    # next()
        

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
            next_img(0)
        # Bottom right
        elif EquX == "more" and EquY == "more":
            EquX = "less"
            EquY = "more"
            next_img(0)


    if root.winfo_y() >= 792:
        print("\033[32mBOTTOM\033[0m")
        # Bottom right
        if EquX == "more" and EquY == "more":
            EquX = "more"
            EquY = "less"
            next_img(0)
        # Bottom left
        elif EquX == "less" and EquY == "more":
            EquX = "less"
            EquY = "less"
            next_img(0)






click()


# Button(text="Bounce?", command=bounce).pack()
# Button(text="switch", command=switch).pack()

next_img(0)

root.mainloop()