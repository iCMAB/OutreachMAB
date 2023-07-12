import tkinter as tk
import tkinter.font as tkFont

class Start_App:

    def __init__(self, root):
        root.title("Restaurant Outreach")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        Start_button=tk.Button(root)
        Start_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=18)
        Start_button["font"] = ft
        Start_button["fg"] = "#000000"
        Start_button["justify"] = "center"
        Start_button["text"] = "Start"
        Start_button.place(x=200,y=220,width=180, height=60)
        Start_button["command"] = self.Start_button_command

        Setting_button=tk.Button(root)
        Setting_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=18)
        Setting_button["font"] = ft
        Setting_button["fg"] = "#000000"
        Setting_button["justify"] = "center"
        Setting_button["text"] = "Settings"
        Setting_button.place(x=200, y=300, width=180, height=60)
        Setting_button["command"] = self.Settings_button_command

        Quit_button=tk.Button(root)
        Quit_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=18)
        Quit_button["font"] = ft
        Quit_button["fg"] = "#000000"
        Quit_button["justify"] = "center"
        Quit_button["text"] = "Quit"
        Quit_button.place(x=200, y=380, width=180, height=60)
        Quit_button["command"] = self.Quit_button_command

        GLabel_950=tk.Label(root)
        ft = tkFont.Font(family='Times', size=38)
        GLabel_950["font"] = ft
        GLabel_950["fg"] = "#333333"
        GLabel_950["justify"] = "center"
        GLabel_950["text"] = "Multi Armed Bandit \n Restaurant Selection"
        GLabel_950.place(x=0, y=60, width=600, height=125)

    def Start_button_command(self):
        print("start")


    def Settings_button_command(self):
        print("settings")


    def Quit_button_command(self):
        print("quit")

if __name__ == "__main__":
    root = tk.Tk()
    app = Start_App(root)
    root.mainloop()
