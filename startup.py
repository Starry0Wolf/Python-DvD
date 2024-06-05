from tkinter import *

root = Tk()
root.title("Pos setter")
root.configure(background="black")
root.minsize(400, 240)
# root.maxsize(400, 240)
root.geometry("300x300+50+50")



def BottomRec():
    print("X:", root.winfo_x(), "Y:", root.winfo_y())
    Bxx = int(root.winfo_x())
    Byy = int(root.winfo_y())
    topDEF()
def TopRec():
    print("X:", root.winfo_x(), "Y:", root.winfo_y())
    Txx = int(root.winfo_x())
    Tyy = int(root.winfo_y())
    rightDEF()
def RightRec():
    print("X:", root.winfo_x(), "Y:", root.winfo_y())
    Rxx = int(root.winfo_x())
    Ryy = int(root.winfo_y())
    leftDEF()
def LeftRec():
    print("X:", root.winfo_x(), "Y:", root.winfo_y())
    Lxx = int(root.winfo_x())
    Lyy = int(root.winfo_y())
    


def bottomDEF():
    Label(
              text="Please aline at the bottom of the screen.\n ↓↓ Click the button when done. ↓↓", 
        
              # Changing font-size here 
              font=("Roboto", 15) 
              ).pack()
    
    Button(text="Please click when alined at the bottom.", font=("Roboto", 20), command=BottomRec, height = 4, width = 50).pack()

def topDEF():
    Label(
              text="Please aline at the top of the screen.\n ↓↓ Click the button when done. ↓↓", 
        
              # Changing font-size here 
              font=("Roboto", 15) 
              ).pack()
    
    Button(text="Please click when alined at the top.", font=("Roboto", 20), command=TopRec, height = 4, width = 50).pack()

def rightDEF():
    Label(
              text="Please aline at the right of the screen.\n ↓↓ Click the button when done. ↓↓", 
        
              # Changing font-size here 
              font=("Roboto", 15) 
              ).pack()
    
    Button(text="Please click when alined at the right.", font=("Roboto", 20), command=RightRec, height = 4, width = 50).pack()

def leftDEF():
    Label(
              text="Please aline at the left of the screen.\n ↓↓ Click the button when done. ↓↓", 
        
              # Changing font-size here 
              font=("Roboto", 15) 
              ).pack()
    
    Button(text="Please click when alined at the left.", font=("Roboto", 20), command=LeftRec, height = 4, width = 50).pack()

bottomDEF()


def WEEE():
    print("X:", root.winfo_x(), "Y:", root.winfo_y())
    # root.after(50, WEEE)

# Button(text="tesWEEt", command=WEEE).pack()



root.mainloop()