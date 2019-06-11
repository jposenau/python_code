'''
Book tracking application desgned to enter books track what's been read 
Created on Jul 5, 2018

@author: jposenau
'''
from tkinter import *

import mysql.connector
from mysql.connector import errorcode
import calendar, datetime
_connection = None

fields = 'title', 'author', 'description', 'acquired date', 'finished date'
class calendarTk(Frame): # class calendarTk
    """ Calendar, the current date is exposed today, or transferred to date"""
    def __init__(self,master=None,date=None,dateformat="%d/%m/%Y",command=lambda i:None):
        Frame.__init__(self, master)
        self.dt=datetime.datetime.now() if date is None else datetime.datetime.strptime(date, dateformat) 
        self.showmonth()
        self.command=command
        self.dateformat=dateformat
    def showmonth(self): # Show the calendar for a month
        sc = calendar.month(self.dt.year, self.dt.month).split('\n')
        for t,c in [('<<',0),('<',1),('>',5),('>>',6)]: # The buttons to the left to the right year and month
            Button(self,text=t,relief='flat',command=lambda i=t:self.callback(i)).grid(row=0,column=c)
        Label(self,text=sc[0]).grid(row=0,column=2,columnspan=3) # year and month
        for line,lineT in [(i,sc[i+1]) for i in range(1,len(sc)-1)]: # The calendar
            for col,colT in [(i,lineT[i*3:(i+1)*3-1]) for i in range(7)]: # For each element
                obj=Button if colT.strip().isdigit() else Label # If this number is a button, or Label
                args={'command':lambda i=colT:self.callback(i)} if obj==Button else {} # If this button, then fasten it to the command
                bg='green' if colT.strip()==str(self.dt.day) else 'SystemButtonFace' # If the date coincides with the day of date - make him a green background
                fg='red' if col>=5 else 'SystemButtonText' # For the past two days, the color red
                obj(self,text="%s"% colT,relief='flat',bg=bg,fg=fg,**args).grid(row=line, column=col, ipadx=2, sticky='nwse') # Draw Button or Label
    def callback(self,but): # Event on the button
        if but.strip().isdigit():  self.dt=self.dt.replace(day=int(but)) # If you clicked on a date - the date change
        elif but in ['<','>','<<','>>']:
            day=self.dt.day
            if but in['<','>']: self.dt=self.dt+datetime.timedelta(days=30 if but=='>' else -30) # Move a month in advance / rewind
            if but in['<<','>>']: self.dt=self.dt+datetime.timedelta(days=365 if but=='>>' else -365) #  Year forward / backward
            try: self.dt=self.dt.replace(day=day) # We are trying to put the date on which stood
            except: pass                          # It is not always possible
        self.showmonth() # Then always show calendar again
        if but.strip().isdigit(): self.command(self.dt.strftime(self.dateformat)) # If it was a date, then call the command

class Booklist_app(Tk):

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
           
            Label(self,text = "PTO Date").grid(row=3,sticky=W)
            e4 = Entry(self, width = 30)
            e4.grid(row = 3 , column = 1) 
          
            Label(self,text = "half or full day").grid(row=4,sticky=W)
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
        top = Toplevel(self)

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
#            c=calendarTk(top,date="21/11/2018",dateformat="%d/%m/%Y",command=calendarTk.com)
#            c.grid(row = 4)
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


    #   label1 = Label(top, text="Results from Query.")
    #    label1.grid(row = 1, column = 0)
        Label(top, text= "Results From Query", font=("Arial",18)).grid(row=0, columnspan=3)
        listbox = Listbox(top, width=80, height = 40, font=('consolas', 12))
        listbox.grid(row=0, column=0)

        b3 = Button(top, text='Quit', command= lambda: top.destroy())
        b3.grid(row = 3)
        yscroll = Scrollbar(top, command=listbox.yview, orient=VERTICAL)
        yscroll.grid(row=0, column=10, sticky=N+S)
        listbox.configure(yscrollcommand=yscroll.set)
        print("in list books")
        cnx = self.get_connection()
        sql = ("Select last_name,  PTO_used, balance  From employee_data")
        header = "    Name        PTO Used       Balance"
        listbox.insert(END, header)
        
        cursora = cnx.cursor(buffered=True)
        cursora.execute(sql)
        for val in cursora:
#          listbox.insert(END,  val) 
            listbox.insert("{:>10}".format(val))         


if __name__ == '__main__':
    
    

    app = Booklist_app(" Book Entry Title")
    app.mainloop()
#    self.mainloop()