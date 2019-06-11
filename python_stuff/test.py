'''
Created on Jul 5, 2018

@author: jposenau
'''
from tkinter import *

if __name__ == '__main__':
    root = Tk()
    root.geometry("500x300")
    root.title("My Book List")

    lab1 = Label(root,text = "Title").grid(row=0,sticky=W)
    e1 = Entry(root, width = 30)
    e1.grid(row = 0 , column = 1)
    
    lab2 = Label(root,text = "Author").grid(row=1,sticky=W)
    e2 = Entry(root, width = 30)
    e2.grid(row = 1 , column = 1)
    
    lab3 = Label(root,text = "Description").grid(row=2,sticky=W)
    e3 = Entry(root, width = 30)
    e3.grid(row = 2 , column =1)
   
    lab6 = Label(root,text = "Acquired Date").grid(row=3,sticky=W)
    e6 = Entry(root, width = 30)
    e6.grid(row = 3 , column = 1) 
    
    lab5 = Label(root,text = "Completed Date").grid(row=3,sticky=W)
    e5 = Entry(root, width = 30)
    e5.grid(row = 3 , column = 1)
    
    b1 = Button(root, text = "List", command = lambda root = root:root.destroy())
    b1.grid(row = 0,column =2)
    b2 = Button(root, text = "Add", command = lambda root = root:root.destroy())
    b2.grid(row = 0,column =3)
    b3 = Button(root, text = "Update", command = lambda root = root:root.destroy())
    b3.grid(row = 0,column =4)
    b4 = Button(root, text = "Show", command = lambda root = root:root.destroy())
    b4.grid(row = 0,column =5)
    b5 = Button(root, text = "Quit", command = lambda root = root:root.destroy())
    b5.grid(row = 0,column =6)
    

   
    root.mainloop()