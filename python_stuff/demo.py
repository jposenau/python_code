'''
Created on Jul 31, 2018

@author: jposenau
'''
import tkinter as tk
import calen2

if __name__ == '__main__':
 
    class Control:
        def __init__(self, parent):
            self.parent = parent
            self.choose_btn = tk.Button(self.parent, text='Choose',command=self.popup)
            self.show_btn = tk.Button(self.parent, text='Show Selected',command=self.print_selected_date)
            self.clear_btn = tk.Button(self.parent, text='Clear Selected',command=self.clear_selected_date)
            self.choose_btn.grid()
            self.show_btn.grid()
            self.clear_btn.grid()
            self.data = {}
             
        def popup(self):
            child = tk.Toplevel()
            cal = calen2.Calendar(child, self.data)
             
        def print_selected_date(self):
            print(self.data)
        def clear_selected_date(self):
            self.data = {}
            print(self.data)
             
 
    root = tk.Tk()
    app = Control(root)
    root.mainloop()
