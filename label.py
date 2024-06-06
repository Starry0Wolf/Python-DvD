from tkinter import *
from PIL import ImageTk, Image
import itertools
import os
import sys


root = Tk()
root.title("DVD")
root.configure(background="black")
root.minsize(402, 180)
root.maxsize(402, 180)
root.geometry("300x300+50+50")

# Create Label in our window


panel = Label(root)
panel.pack()


script_dir = os.path.dirname(sys.argv[0])

image1_path = os.path.join(script_dir, '_internal', 'download-1.png')
image2_path = os.path.join(script_dir, '_internal', 'download-2.png')
image3_path = os.path.join(script_dir, '_internal', 'download-3.png')
image4_path = os.path.join(script_dir, '_internal', 'download-4.png')
image5_path = os.path.join(script_dir, '_internal', 'download-5.png')
image6_path = os.path.join(script_dir, '_internal', 'download-6.png')
image7_path = os.path.join(script_dir, '_internal', 'download-7.png')

# , 'dvdlogo-02.jpeg', 'dvdlogo-03.jpeg', 'dvdlogo-04.jpeg', 'dvdlogo-05.jpeg', 'dvdlogo-06.jpeg', 'dvdlogo-07.jpeg'
images = [image1_path, image2_path, image3_path, image4_path, image5_path, image6_path, image7_path]
images = iter(images)  # make an iterator
images = itertools.cycle(images)


# TheSIZE = 400, 240
# output_dir = "wooo/"
# for img_path in images:
#     with Image.open(img_path) as img:
#         img.thumbnail(TheSIZE)
#         new_img_path = os.path.join(output_dir, os.path.basename(img_path))
#         img.save(new_img_path)


def next_img():
    try:
        img = next(images)  # get the next image from the iterator
        # root.after(next_img, timeNOW)
        
    except StopIteration:
        return  # if there are no more images, do nothing

    # load the image and display it
    
    img = Image.open(img)
    img = ImageTk.PhotoImage(img)
    panel.img = img  # keep a reference so it's not garbage collected
    panel['image'] = img



screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
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
    # print("X:", root.winfo_x(), "Y:", root.winfo_y(), "  EquX:", EquX, "EquY:", EquY) # DEBUG FEATHURE!
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
        # print("\033[32mLEFT\033[0m")
        # Bottom left
        if EquX == "less" and EquY == "more":
            EquX = "more"
            EquY = "more"
            next_img()
        # Top left
        elif EquX == "less" and EquY == "less":
            EquX = "more"
            EquY = "less"
            next_img()


    if root.winfo_y() <= 25:
        # print("\033[32mTOP\033[0m")
        # Top right
        if EquX == "more" and EquY == "less":
            EquX = "more"
            EquY = "more"
            next_img()
        # Top left
        elif EquX == "less" and EquY == "less":
            EquX = "less"
            EquY = "more"
            next_img()

    # next()
        

# To top left is both negtive
# To bottom right is both postive
# To top right is x postive and y negtive
# To bottom left is x negtive and y postive


    if root.winfo_x() >= screen_width:
        # print("\033[32mRIGHT\033[0m")
        # Top right
        if EquX == "more" and EquY == "less":
            EquX = "less"
            EquY = "less"
            next_img()
        # Bottom right
        elif EquX == "more" and EquY == "more":
            EquX = "less"
            EquY = "more"
            next_img()


    if root.winfo_y() >= screen_height:
        # print("\033[32mBOTTOM\033[0m")
        # Bottom right
        if EquX == "more" and EquY == "more":
            EquX = "more"
            EquY = "less"
            next_img()
        # Bottom left
        elif EquX == "less" and EquY == "more":
            EquX = "less"
            EquY = "less"
            next_img()






click()


# Button(text="Bounce?", command=bounce).pack()
# Button(text="switch", command=switch).pack()

next_img()

root.mainloop()