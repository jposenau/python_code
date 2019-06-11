'''
Created on Jul 5, 2018

@author: jposenau
'''
from tkinter import *
import mysql.connector
from mysql.connector import errorcode

_connection = None

fields = 'title', 'author', 'description', 'acquired date', 'finished date'
class SampleApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
#        self = self.Tk()
        self.geometry("500x300")
        self.title("My Book List")
        vals = []
        lab1 = Label(self,text = "Title").grid(row=0,sticky=W)
        e1 = Entry(self, width = 30)
        e1.grid(row = 0 , column = 1)
        1
        lab2 = Label(self,text = "Author").grid(row=1,sticky=W)
        e2 = Entry(self, width = 30)
        e2.grid(row = 1 , column = 1)
       
        lab3 = Label(self,text = "Description").grid(row=2,sticky=W)
        e3 = Entry(self, width = 30)
        e3.grid(row = 2 , column =1)
       
        lab6 = Label(self,text = "Acquired Date").grid(row=3,sticky=W)
        e4 = Entry(self, width = 30)
        e4.grid(row = 3 , column = 1) 
      
        lab5 = Label(self,text = "Completed Date").grid(row=4,sticky=W)
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
    def get_val(self,e1):
        print("in get val")
        top = Toplevel(self)
        label1 = Label(top, text="Results from Search.")
        label1.pack()
        listbox = Listbox(top, width=60)
        listbox.pack()
        b3 = Button(top, text='Quit', command= lambda: top.destroy())
        b3.pack()
        v1 = e1.get()
        e1.delete(0,END) 
        print("in Search", v1)
        cnx = self.get_connection()
        sql = ("Select title From books where title = '%s' " %v1)
        cursora = cnx.cursor(buffered=True)
        cursora.execute(sql)
        for val in cursora:
            listbox.insert(END,  val)            
         
                 
    def update(self):
        top = Toplevel(self)
        top.title = "Update Screen"
        lab1 = Label(top,text = "Enter Title", font = (('Times'),12))
        lab1.grid(row = 0, column = 0,sticky =W)
        e1 = Entry(top, width = 40)
        e1.grid(row = 0 , column = 1)
        b1 = Button(top, text = "Search", command = lambda self = self:self.get_val(e1))
        b1.grid(row = 0,column =2)
        b5 = Button(top, text = "Quit", command= lambda: top.destroy())
        b5.grid(row = 0,column =6)
        
        
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
        label1 = Label(top, text="Results from Query.")
        label1.pack()
        listbox = Listbox(top, width=60)
        listbox.pack()
        b3 = Button(top, text='Quit', command= lambda: top.destroy())
        b3.pack()
        print("in list books")
        cnx = self.get_connection()
        sql = ("Select * From books")
        cursora = cnx.cursor(buffered=True)
        cursora.execute(sql)
        for val in cursora:
            listbox.insert(END,  val)            


if __name__ == '__main__':
    
    

    app = SampleApp()
    app.mainloop()
#    self.mainloop()