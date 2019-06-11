'''
Book tracking application desgned to enter books track what's been read 
Created on Jul 5, 2018

@author: jposenau
'''
from tkinter import *

import mysql.connector
from mysql.connector import errorcode
import calen
_connection = None


class Leave_mgr_app(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
#        self = self.Tk()
        self.geometry("500x300")
        self.title("Employee Entry ")
        self.main_menu()
    
    def   main_menu(self):
        
        
            Label(self,text = "Manager").grid(row=0,sticky=W)
            e1 = Entry(self, width = 30)
            e1.grid(row = 0 , column = 1)
            1
            Label(self,text = "Name").grid(row=1,sticky=W)
            e2 = Entry(self, width = 30)
            e2.grid(row = 1 , column = 1)
           
            Label(self,text = "DOH").grid(row=2,sticky=W)
            e3 = Entry(self, width = 30)
            e3.grid(row = 2 , column =1)
            
            Label(self,text = "Balance").grid(row=3,sticky=W)
            e4 = Entry(self, width = 30)
            e4.grid(row = 3 , column =1)
            
            Label(self,text = "PTO Used").grid(row=4,sticky=W)
            e5 = Entry(self, width = 30)
            e5.grid(row = 4 , column =1)
            
            Label(self,text = "PTO Accrued").grid(row=5,sticky=W)
            e6 = Entry(self, width = 30)
            e6.grid(row = 5 , column =1)
           
            Label(self,text = "PTO Date").grid(row=6,sticky=W)
            e7 = Entry(self, width = 30)
            e7.grid(row = 6 , column = 1) 
          
            Label(self,text = "Half or full day").grid(row=7,sticky=W)
            e8 = Entry(self, width = 30)
            e8.grid(row = 7 , column = 1)
            
            b1 = Button(self, text = "List", command = lambda self = self:self.find_emp(e1,e2,e3,e4,e5,e6,e7,e8))
            b1.grid(row = 0,column =2)
            b2 = Button(self, text = "Add", command = lambda self = self:self.entry(e1,e2,e3,e4,e5))
            b2.grid(row = 0,column =3)
            b3 = Button(self, text = "Update", command = lambda self = self:self.update())
            b3.grid(row = 0,column =4)
            b4 = Button(self, text = "Show", command =  lambda self  = self:self.callback(e1,e2,e3,e4,e5))
            b4.grid(row = 0,column =5)
            b5 = Button(self, text = "Clear", command = lambda self = self:self.clearit(e1,e2,e3,e4,e5,e6))
            b5.grid(row = 0,column =6)
            b6 = Button(self, text = "Quit", command = lambda self = self:self.destroy())
            b6.grid(row = 0,column =7)
        
    def putit(self,dd):
        print(dd)
    def callback(self, e1,e2,e3,e4,e5):
        vals = []
        
        vals.append( (e1.get()))
        vals.append(e2.get())
        vals.append(e3.get())
        vals.append(e4.get())
        vals.append(e5.get())
        print (vals)
        
    def clearit(self, e1,e2,e3,e4,e5,e6):
        e1.delete(0,END) 
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END) 
        e6.delete(0,END) 
        
        
    def get_val(self,e1):
        vals = []

        top = Toplevel(self)
        label1 = Label(top, text="Results from Search.")
        label1.grid(row = 1)
        listbox = Listbox(top, width=60)
        listbox.grid(row = 5)
        b3 = Button(top, text='Quit', command= lambda: top.destroy())
        b3.grid(row = 3)
        v1 = e1.get()
 
        print("in Search", v1,v2)
        cnx = self.get_connection()
        sql = ("Select Last_name, PTO_used, balance From employee_data where `last_name` = '%s' " %v1)
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
        top.geometry("500x500")
        lab1 = Label(top,text = "Enter Date for PTO", font = (('Times'),12))
        lab1.grid(row = 0, column = 0,sticky =W)
        calen.Datepicker(top).grid(sticky = W, row = 10)  

        b5 = Button(top, text = "Quit", command= lambda: top.destroy())
        b5.grid(row = 0,column =6)
        
    def entry_update(self,vals):
#  Prepare a statement for an uppdate
        print("entry_update")
       
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
        
    def find_emp(self,e1,e2,e3,e4,e5,e6,e7,e8):

        v = e2.get()
        param = v

        
        print("in list books")
        cnx = self.get_connection()

        cursora = cnx.cursor(buffered=True)
        cursora.execute("Select Manager,Last_name,doh,balance,PTO_used,PTO_accrued  from employee_data WHERE Last_name LIKE  %s ", (param + "%",))
        for val in cursora:
            print(val)
            e1.delete(0,END)
            e1.insert(0,val[0])
            e2.delete(0,END)
            e2.insert(0,val[1])
            e3.delete(0,END)
            e3.insert(0,val[2])
            e4.delete(0,END)
            e4.insert(0,val[3])
            e5.delete(0,END)
            e5.insert(0,val[4])
            e6.delete(0,END)
            e6.insert(0,val[5])
#            listbox.insert(END,  val) 
                


if __name__ == '__main__':
    
    

    app = Leave_mgr_app(" Leave Managment")
    app.mainloop()
#    self.mainloop()