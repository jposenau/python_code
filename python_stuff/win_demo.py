from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
#Creation of init_window
    def init_window(self):

# changing the title of our master widget      
        self.master.title("GUI ")

# allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

# creating a button instance
        quitButton = Button(self, text="Quit")
        self.pack(fill=BOTH, expand=1)

# placing the button on my window
        quitButton.place(x=0, y=0)
        
root = Tk( )
root.geometry("400x300")
app = Window(root) 
  
root.mainloop()    