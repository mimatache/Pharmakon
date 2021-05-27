from tkinter import *
from drug import ChooseDrug


window = Tk()

def Start():
    Title = Label(window, text = "Pharmakon")
    Title.pack()

    desribeButton = Button(window, text = "Describe Drug", fg = "darkgreen", bg = "white")
    desribeButton.pack()
    

    
    window.mainloop()






