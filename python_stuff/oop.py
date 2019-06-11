'''
Created on Jun 29, 2018

@author: jposenau
'''
# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/    

import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
import mysql.connector
from datetime import date, datetime, timedelta
from mysql.connector import errorcode

_connection = None
fields = 'title', 'author', 'description', 'acquired date', 'finished date'
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.frames["StartPage"] = StartPage(parent=container, controller=self)
        self.frames["PageOne"] = PageOne(parent=container, controller=self)
        self.frames["PageTwo"] = PageTwo(parent=container, controller=self)
        self.frames["PageThree"] = PageThree(parent=container, controller=self)
        self.frames["PageFour"] = PageFour(parent=container, controller=self)
        
        self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageOne"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageTwo"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageThree"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageFour"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        self.get_connection()

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
   

    def get_connection(self):
        global _connection
        if not _connection:
            _connection = mysql.connector.connect(user='jposenau',
            database='mine',
            password = 'Dadrules503',
            host = '127.0.0.1' )
        return _connection   
    def close_out(self): 
        print("in closeout")
        self.destroy()
   
    
        
    def entry(self, entries):   
        vals = []

        for entry in entries:
    #        field = entry[0]
            vals.append(entry[1].get())
        print(vals)
        title = vals[0]
        author = vals[1]
        description= vals[2]
        acq = vals[3]
        finished = vals[4]    
        try:
    
            add_employee = ("INSERT INTO books "
            "(title, author, description, acq, finished) "
            "VALUES (%s, %s, %s, %s, %s)")
            data_employee = (title,author,description, acq, finished)
    
            cnx = self.get_connection()
            cursor = cnx.cursor()
            cursor.execute(add_employee, data_employee) 
    
            cnx.commit()
            print ("Entry committed")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
      
       
    def list_books(self):
        top = tk.Toplevel(self)
        label1 = tk.Label(top, text="Results from Query.")
        label1.pack()
        listbox = tk.Listbox(top, width=60)
        listbox.pack()
        b3 = tk.Button(top, text='Quit', command= lambda: top.destroy())
        b3.pack(side=tk.LEFT, padx=5, pady=5)
        print("in list books")
        cnx = self.get_connection()
        sql = ("Select * From books")
        cursora = cnx.cursor(buffered=True)
        cursora.execute(sql)
        for val in cursora:
            listbox.insert(tk.END,  val)           
    

class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to Book list Management", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        fields = 'title', 'author', 'description', 'acquired date', 'finished date'
        entries = []
            
            
        button1 = tk.Button(self, text="Add Entries",
                            command=lambda: controller.makeform())
        button2 = tk.Button(self, text="List Entries",
                            command=lambda: controller.list_books())
        button3 = tk.Button(self, text="Show Entries",
                            command=lambda: controller.show_frame("PageThree"))
        button4 = tk.Button(self, text="Update",
                            command=lambda: controller.show_frame("PageFour"))
        button5 = tk.Button(self, text="Quit",
                            command=lambda: controller.close_out())
        button1.grid(row =0 , column = 1)
        button2.grid(row =1 , column = 1)
        button3.grid(row =2 , column =1 )
        button4.grid(row =3 , column = 1)
        button5.grid(row =4 , column = 1)
#        row = tk.Frame(self)
#        row.pack(side = tk.BOTTOM)
#    #   for field in fields[0]:
         
        
       
#            row.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
        
    

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Return to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Return to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 3", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Return to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 4", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Return to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()