import time
import asyncio
import random
from tkinter import *
from PIL import ImageTk, Image
import itertools
import os


root = Tk()
root.title("DVD")
root.configure(background="black")
root.minsize(402, 180)
root.maxsize(402, 180)
root.geometry("300x300+50+50")

# Create Label in our window
# image = PhotoImage(file="/Users/jamescady/Desktop/Coding_stuff/Window_Game/PythonDVD/logo.png")

panel = Label(root)
panel.pack()
# folderr22=str("C:/Users/Person/Downloads/Python-DvD-main/Python-DvD-main/Version2/new/Cloudconvert/download-")
folderr22=str("C:/Users/Person/Downloads/Python-DvD-main/Python-DvD-main/wooo/download-")




# file="/Users/jamescady/Desktop/Coding_stuff/Window_Game/Version2/Cloudconvert
# , 'dvdlogo-02.jpeg', 'dvdlogo-03.jpeg', 'dvdlogo-04.jpeg', 'dvdlogo-05.jpeg', 'dvdlogo-06.jpeg', 'dvdlogo-07.jpeg'
images = [folderr22 + "1.png", folderr22 + "2.png", folderr22 + "3.png", folderr22 + "4.png", folderr22 + "5.png", folderr22 + "6.png", folderr22 + "7.png"]
images = iter(images)  # make an iterator
images = itertools.cycle(images)


# TheSIZE = 400, 240
# output_dir = "wooo/"
# for img_path in images:
#     with Image.open(img_path) as img:
#         img.thumbnail(TheSIZE)
#         new_img_path = os.path.join(output_dir, os.path.basename(img_path))
#         img.save(new_img_path)


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



screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_height, screen_width)
screen_height -= 250
screen_width -= 400


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
            next_img(1)
        # Top left
        elif EquX == "less" and EquY == "less":
            EquX = "more"
            EquY = "less"
            next_img(1)


    if root.winfo_y() <= 25:
        print("\033[32mTOP\033[0m")
        # Top right
        if EquX == "more" and EquY == "less":
            EquX = "more"
            EquY = "more"
            next_img(1)
        # Top left
        elif EquX == "less" and EquY == "less":
            EquX = "less"
            EquY = "more"
            next_img(1)

    # next()
        

# To top left is both negtive
# To bottom right is both postive
# To top right is x postive and y negtive
# To bottom left is x negtive and y postive


    if root.winfo_x() >= screen_width:
        print("\033[32mRIGHT\033[0m")
        # Top right
        if EquX == "more" and EquY == "less":
            EquX = "less"
            EquY = "less"
            next_img(1)
        # Bottom right
        elif EquX == "more" and EquY == "more":
            EquX = "less"
            EquY = "more"
            next_img(1)


    if root.winfo_y() >= screen_height:
        print("\033[32mBOTTOM\033[0m")
        # Bottom right
        if EquX == "more" and EquY == "more":
            EquX = "more"
            EquY = "less"
            next_img(1)
        # Bottom left
        elif EquX == "less" and EquY == "more":
            EquX = "less"
            EquY = "less"
            next_img(1)






click()


# Button(text="Bounce?", command=bounce).pack()
# Button(text="switch", command=switch).pack()

next_img(1)

root.mainloop()