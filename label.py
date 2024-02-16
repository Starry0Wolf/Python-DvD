import time
import asyncio
import operator
from tkinter import *

root = Tk()
root.title("DVD")
root.configure(background="black")
root.minsize(400, 240)
# root.maxsize(400, 240)
root.geometry("300x300+50+50")
# a = 1
# b = 2
# def show_alert():
#     print(f"3333 {root.geometry}")
#     root.geometry(f'+{a}+{b}')

# Tk.Button(root, text="Click Me", command=show_alert).pack()
# Postion and size getter



# Edges
    # Top_Left is x=0 y=25
    # Bottom_Left is x=0 y=833
    # Bottom_Right is x=1648 y=833
    # Top_right is x=1648 y=25

# Sides
    # Top is y=25
    # Bottom is y=833
    # Left is x=0
    # Right is x=1648

# Create Label in our window
image = PhotoImage(file="PythonDvD/logo.png")
image2 = image.subsample(3,3)
img = Label(root, image=image2)
img.pack()


# def OLD_STUFF(Yeah):

    # ops = {
    #         "+": operator.add,
    #         "-": operator.sub,
    # }   
    # op_char = "+"
    # op_func = ops[op_char]
    # result = op_func()

global xx
global yy
xx = 825
yy = 436

# To top left is both negtive
# To bottom right is both postive
# To top right is x postive and y negtive
# To bottom left is y postive and x negtive
EquX = "-="
EquY = "+="
global event4
direction_changed = False

def configure_handler(event4):
    global EquX
    global EquY
    print(event4)
    if event4 == "x=745":
        EquX = "+="
    EquY = "-="
    
    # root.after_idle(move22)

root.bind("<Configure>", configure_handler)

def move22():
    global xx
    global yy
    global EquX
    global EquY
    
    if EquX == "-=":
        xx -= 10
    elif EquX == "+=":
        xx += 10
    
    if EquY == "-=":
        yy -= 10
    elif EquY == "+=":
        yy += 10

    root.geometry(f'+{xx}+{yy}')
    root.update


Button(root, text="Click Me", command=move22).pack()
# asyncio.run(hello())
root.mainloop()
