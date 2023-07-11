import tkinter as tk
import tkinter.font as tkFont
from .simulator import Simulator

class App:
    rightButton = tk.Button
    currentIter = tk.Label
    leftButton = tk.Button
    def __init__(self, root):
        simulation = Simulator("../config")
        root.title("Restaurant Outreach")
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        #Variables for labels
        self.integer = tk.IntVar()
        self.integer.set(1)

        self.restaurantNum = "Selection: Restaurant #"

        rightButton = tk.Button(root)
        rightButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=30)
        rightButton["font"] = ft
        rightButton["fg"] = "#000000"
        rightButton["justify"] = "center"
        rightButton["text"] = ">"
        rightButton.place(x=390,y=370,width=140,height=80)
        rightButton["command"] = self.increaseCommand

        currentIter=tk.Label(root, textvariable=str(self.integer))
        ft = tkFont.Font(family='Times', size=50)
        currentIter["font"] = ft
        currentIter["fg"] = "#333333"
        currentIter["justify"] = "center"
        currentIter.place(x=230, y=370, width=131, height=65)

        leftButton=tk.Button(root)
        leftButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=30)
        leftButton["font"] = ft
        leftButton["fg"] = "#000000"
        leftButton["justify"] = "center"
        leftButton["text"] = "<"
        leftButton.place(x=60, y=370, width=140, height=80)
        leftButton["command"] = self.decreaseCommand

        GLabel_6 = tk.Label(root, textvariable=str(self.restaurantNum))
        ft = tkFont.Font(family='Times', size=23)
        GLabel_6["font"] = ft
        GLabel_6["fg"] = "#333333"
        GLabel_6["justify"] = "left"
        GLabel_6.place(x=60, y=90, width=300, height=40)

        GLabel_411 = tk.Label(root, textvariable=str(self.reward))
        ft = tkFont.Font(family='Times', size=23)
        GLabel_411["font"] = ft
        GLabel_411["fg"] = "#333333"
        GLabel_411["justify"] = "left"
        GLabel_411.place(x=60, y=150, width=300, height=40)

        GLabel_582 = tk.Label(root, textvariable=str(self.regret))
        ft = tkFont.Font(family='Times', size=23)
        GLabel_582["font"] = ft
        GLabel_582["fg"] = "#333333"
        GLabel_582["justify"] = "left"
        GLabel_582.place(x=60, y=210, width=300, height=40)

    def increaseCommand(self):
        self.integer.set(self.integer.get() + 1)


    def decreaseCommand(self):
        self.integer.set(self.integer.get() - 1)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
