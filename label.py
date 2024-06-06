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

# image1_path = os.path.join(script_dir, '_internal', 'download-1.png')
# image2_path = os.path.join(script_dir, '_internal', 'download-2.png')
# image3_path = os.path.join(script_dir, '_internal', 'download-3.png')
# image4_path = os.path.join(script_dir, '_internal', 'download-4.png')
# image5_path = os.path.join(script_dir, '_internal', 'download-5.png')
# image6_path = os.path.join(script_dir, '_internal', 'download-6.png')
# image7_path = os.path.join(script_dir, '_internal', 'download-7.png')

image1_path = os.path.join(script_dir, 'download-1.png')
image2_path = os.path.join(script_dir, 'download-2.png')
image3_path = os.path.join(script_dir, 'download-3.png')
image4_path = os.path.join(script_dir, 'download-4.png')
image5_path = os.path.join(script_dir, 'download-5.png')
image6_path = os.path.join(script_dir, 'download-6.png')
image7_path = os.path.join(script_dir, 'download-7.png')

# , 'dvdlogo-02.jpeg', 'dvdlogo-03.jpeg', 'dvdlogo-04.jpeg', 'dvdlogo-05.jpeg', 'dvdlogo-06.jpeg', 'dvdlogo-07.jpeg'
images = [image1_path, image2_path, image3_path, image4_path, image5_path, image6_path, image7_path]
images = iter(images)  # make an iterator
images = itertools.cycle(images)

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

EquX = "less"
EquY = "more"

ThEsPEED = input("What speed? High is slow, low is fast, no decmails.\n")

# def tester(ipute):
#     global ThEsPEED
#     ThEsPEED = 0
#     if ipute == str():
#         ipute = input("What speed? High is slow, low is fast, no decmails.\n")
#         tester(ipute)
#     else:
#         ThEsPEED = ipute
    
# BEEPW = input("What speed? High is slow, low is fast, no decmails.\n")
# if BEEPW == str():
#     tester()
# else:
#     BEEPW = ThEsPEED

moveAmount = 1
def click():
    global EquX
    global EquY
    global moveAmount
    # print("X:", root.winfo_x(), "Y:", root.winfo_y(), "  EquX:", EquX, "EquY:", EquY) # DEBUG FEATHURE!
    xx = int(root.winfo_x())
    yy = int(root.winfo_y())

    if EquX == "less":
        xx -= moveAmount
    elif EquX == "more":
        xx += moveAmount
    
    if EquY == "less":
        yy -= moveAmount
    elif EquY == "more":
        yy += moveAmount

    root.geometry(f'+{xx}+{yy}')
    root.update
    bounce()
    root.after(ThEsPEED, click)


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

next_img()

root.mainloop()