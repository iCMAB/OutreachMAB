import tkinter as tk
import tkinter.font as tkFont
#from .simulator import Simulator

class App:
    rightButton = tk.Button
    currentIter = tk.Label
    leftButton = tk.Button
    def __init__(self, root):
        #simulation = Simulator("../config")
        root.title("Restaurant Outreach")
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        #Variables for labels
        self.iter = tk.IntVar()
        self.iter.set(1)

        self.restaurantNum = tk.StringVar()
        self.restaurantNum.set("Selected: Restaurant #")

        self.reward = tk.StringVar()
        self.reward.set("Reward: ")

        self.regret = tk.StringVar()
        self.regret.set("Regret: ")


        rightButton = tk.Button(root)
        rightButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=30)
        rightButton["font"] = ft
        rightButton["fg"] = "#000000"
        rightButton["justify"] = "center"
        rightButton["text"] = ">"
        rightButton.place(x=390,y=370,width=140,height=80)
        rightButton["command"] = self.increaseCommand

        currentIter=tk.Label(root, textvariable=str(self.iter))
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

        selectionLabel = tk.Label(root, textvariable=str(self.restaurantNum))
        ft = tkFont.Font(family='Times', size=23)
        selectionLabel["font"] = ft
        selectionLabel["fg"] = "#333333"
        selectionLabel["justify"] = "left"
        selectionLabel.place(x=60, y=90, width=300, height=40)

        rewardLabel = tk.Label(root, textvariable=str(self.reward))
        ft = tkFont.Font(family='Times', size=23)
        rewardLabel["font"] = ft
        rewardLabel["fg"] = "#333333"
        rewardLabel["justify"] = "left"
        rewardLabel.place(x=60, y=150, width=300, height=40)

        regretLabel = tk.Label(root, textvariable=str(self.regret))
        ft = tkFont.Font(family='Times', size=23)
        regretLabel["font"] = ft
        regretLabel["fg"] = "#333333"
        regretLabel["justify"] = "left"
        regretLabel.place(x=60, y=210, width=300, height=40)

    def increaseCommand(self):
        self.iter.set(self.iter.get() + 1)


    def decreaseCommand(self):
        if (self.iter.get() > 1):
            self.iter.set(self.iter.get() - 1)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
