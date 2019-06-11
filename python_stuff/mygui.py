'''
Book tracking application desgned to enter books track what's been read 
Created on Jul 5, 2018

@author: jposenau
'''
from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import errorcode

_connection = None

fields = 'title', 'author', 'description', 'acquired date', 'finished date'
class Booklist_app(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
#        self = self.Tk()
        self.geometry("500x300")
        self.title("Book Entry ")
        self.main_menu()
    
    def   main_menu(self):
        
        
            Label(self,text = "Title").grid(row=0,sticky=W)
            e1 = Entry(self, width = 30)
            e1.grid(row = 0 , column = 1)
            1
            Label(self,text = "Author").grid(row=1,sticky=W)
            e2 = Entry(self, width = 30)
            e2.grid(row = 1 , column = 1)
           
            Label(self,text = "Description").grid(row=2,sticky=W)
            e3 = Entry(self, width = 30)
            e3.grid(row = 2 , column =1)
           
            Label(self,text = "Acquired Date").grid(row=3,sticky=W)
            e4 = Entry(self, width = 30)
            e4.grid(row = 3 , column = 1) 
          
            Label(self,text = "Completed Date").grid(row=4,sticky=W)
            e5 = Entry(self, width = 30)
            e5.grid(row = 4 , column = 1)
            
            b1 = Button(self, text = "List", command = lambda self = self:self.list_books())
            b1.grid(row = 0,column =2)
            b2 = Button(self, text = "Add", command = lambda self = self:self.entry(e1,e2,e3,e4,e5))
            b2.grid(row = 0,column =3)
            b3 = Button(self, text = "Update", command = lambda self = self:self.update())
            b3.grid(row = 0,column =4)
            b4 = Button(self, text = "Show", command =  lambda self  = self:self.callback(e1,e2,e3,e4,e5))
            b4.grid(row = 0,column =5)
            b5 = Button(self, text = "Quit", command = lambda self = self:self.destroy())
            b5.grid(row = 0,column =6)
        
    def callback(self, e1,e2,e3,e4,e5):
        vals = []
        
        vals.append( (e1.get()))
        vals.append(e2.get())
        vals.append(e3.get())
        vals.append(e4.get())
        vals.append(e5.get())
        print (vals)
        
        
        
    def get_val(self,e1,e2):
        vals = []

        top = Toplevel(self)
        label1 = Label(top, text="Results from Search.")
        label1.grid(row = 1)
        listbox = Listbox(top, width=60)
        listbox.grid(row = 5)
        b3 = Button(top, text='Quit', command= lambda: top.destroy())
        b3.grid(row = 3)
        v1 = e1.get()
        e1.delete(0,END)
        v2 = e2.get()
        e2.delete(0,END)  
        print("in Search", v1,v2)
        cnx = self.get_connection()
        sql = ("Select * From books where `index` = '%s' " %v1)
        cursora = cnx.cursor(buffered=True)
        cursora.execute(sql)

        for val in cursora:
            listbox.insert(END, val)
            vals.append(val)
        print(vals)
        self.entry_update(vals)
          
         
                 
    def update(self):
        top = Toplevel(self)
        top.title = "Update Screen"
        lab1 = Label(top,text = "Enter Index to update", font = (('Times'),12))
        lab1.grid(row = 0, column = 0,sticky =W)
        lab2 = Label(top,text = "Enter Updated Title", font = (('Times'),12))
        lab2.grid(row = 2, column = 0,sticky =W)
        e1 = Entry(top, width = 40)
        e1.grid(row = 0 , column = 1)
        e2 = Entry(top, width = 40)
        e2.grid(row = 2 , column = 1)
        b1 = Button(top, text = "Search", command = lambda self = self:self.get_val(e1,e2))
        b1.grid(row = 0,column =2)
        b5 = Button(top, text = "Quit", command= lambda: top.destroy())
        b5.grid(row = 0,column =6)
        
    def entry_update(self,vals):
#  Prepare a statement for an uppdate
        print(vals)
        

#    Build the query
#        title = vals[0]
#        author = vals[1]
#        description= vals[2]
#        acq = vals[3]
#        finished = vals[4] 
# Clear the entry fields
 
        try:
    
#            add_employee = ("INSERT INTO books "
#            "(title, author, description, acq, finished) "
#            "VALUES (%s, %s, %s, %s, %s)")
#            data_employee = (title,author,description, acq, finished)
    
#            cnx = self.get_connection()
#            cursor = cnx.cursor()
#            cursor.execute(add_employee, data_employee) 
    
#            cnx.commit()
            print ("Entry committed")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)   
    def entry(self,e1,e2,e3,e4,e5):

        vals = []
        
        vals.append( (e1.get()))
        vals.append(e2.get())
        vals.append(e3.get())
        vals.append(e4.get())
        vals.append(e5.get())
#    Build the query
        title = vals[0]
        author = vals[1]
        description= vals[2]
        acq = vals[3]
        finished = vals[4] 
# Clear the entry fields
        e1.delete(0,END) 
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END) 
     
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
        
    def list_books(self):
        top = Toplevel(self)


#        label1 = Label(top, text="Results from Query.")
#        label1.grid(row = 1, column = 0)
        Label(top, text= "Results From Query", font=("Arial",18)).grid(row=0, columnspan=3)
        listbox = Listbox(top, width=80, height = 20, font=('consolas', 12))
        listbox.grid(row=0, column=0)

        b3 = Button(top, text='Quit', command= lambda: top.destroy())
        b3.grid(row = 3)
        yscroll = Scrollbar(top, command=listbox.yview, orient=VERTICAL)
        yscroll.grid(row=0, column=10, sticky=N+S)
        listbox.configure(yscrollcommand=yscroll.set)
        print("in list books")
        cnx = self.get_connection()
        sql = ("Select * From books")
        header = "    Title    Author    Description"
        listbox.insert(END, header)
        cursora = cnx.cursor(buffered=True)
        cursora.execute(sql)
        for val in cursora:
            listbox.insert(END,  val)            


if __name__ == '__main__':
    
    

    app = Booklist_app(" Book Entry Title")
    app.mainloop()
#    self.mainloop()