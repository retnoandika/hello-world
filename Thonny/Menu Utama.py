import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_377=tk.Label(root)
        ft = tkFont.Font(family='Times',size=23)
        GLabel_377["font"] = ft
        GLabel_377["fg"] = "#333333"
        GLabel_377["justify"] = "center"
        GLabel_377["text"] = "Accounting "
        GLabel_377.place(x=160,y=0,width=273,height=57)

        GButton_955=tk.Button(root)
        GButton_955["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_955["font"] = ft
        GButton_955["fg"] = "#000000"
        GButton_955["justify"] = "center"
        GButton_955["text"] = "General Ladger"
        GButton_955.place(x=70,y=70,width=191,height=108)
        GButton_955["command"] = self.GButton_955_command

        GButton_802=tk.Button(root)
        GButton_802["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_802["font"] = ft
        GButton_802["fg"] = "#000000"
        GButton_802["justify"] = "center"
        GButton_802["text"] = "Laporan Rugi Laba"
        GButton_802.place(x=340,y=70,width=187,height=107)
        GButton_802["command"] = self.GButton_802_command

        GButton_901=tk.Button(root)
        GButton_901["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_901["font"] = ft
        GButton_901["fg"] = "#000000"
        GButton_901["justify"] = "center"
        GButton_901["text"] = "Ganti Password"
        GButton_901.place(x=210,y=240,width=191,height=107)
        GButton_901["command"] = self.GButton_901_command

        GButton_843=tk.Button(root)
        GButton_843["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_843["font"] = ft
        GButton_843["fg"] = "#000000"
        GButton_843["justify"] = "center"
        GButton_843["text"] = "Keluar"
        GButton_843.place(x=490,y=440,width=70,height=25)
        GButton_843["command"] = self.GButton_843_command

    def GButton_955_command(self):
        print("command")


    def GButton_802_command(self):
        print("command")


    def GButton_901_command(self):
        print("command")


    def GButton_843_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()