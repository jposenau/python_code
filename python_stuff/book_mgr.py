'''
Created on Jun 27, 2018

@author: jposenau
'''
# Simple enough, just import everything from tkinter.

from tkinter import *
import mysql.connector
from datetime import date, datetime, timedelta
from mysql.connector import errorcode

_connection = None
fields = 'title', 'author', 'description', 'acquired date', 'finished date'

def get_connection():
    global _connection
    if not _connection:
        _connection = mysql.connector.connect(user='jposenau',
        database='mine',
        password = 'Dadrules503',
        host = '127.0.0.1' )
    return _connection        
def fetch(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()

        print('%s: "%s"' % (field, text)) 

def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text=field, anchor='w')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))
    return entries

def list_books(root):
    top = Toplevel(root)
    label1 = Label(top, text="Results from Query.")
    label1.pack()
    listbox = Listbox(top, width = 50)
    listbox.pack(fill = BOTH, expand = YES)
    b3 = Button(top, text='Quit', command=top.destroy)
    b3.pack(side=LEFT, padx=5, pady=5)
    print("in list books")
    cnx = get_connection()
    sql = ("Select * From books")
    cursora = cnx.cursor(buffered=True)
    cursora.execute(sql)
    for val in cursora:
        listbox.insert(END,val)
        print(val)
        
        
def update(entries):
    print("In Update")
    vals = []

    for entry in entries:
#        field = entry[0]
        vals.append(entry[1].get())
    print(vals)

def entry(entries):
# Build the entry string and push to db   
  
    today = datetime.now().date()
    vals = []

    for entry in entries:
        vals.append(entry[1].get())
        entry[1].delete(0,END)
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

        cnx = get_connection()
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


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300")
    root.title("My Book List")
    ents = makeform(root, fields)
#    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    b1 = Button(root, text='Show',
        command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5) 
    b2 = Button(root, text='Enter', command = (lambda e=ents: entry(e)))
    b2.pack(side=LEFT, padx=5, pady=5)
    b4 = Button(root, text = 'List', command = (lambda e=ents: list_books(root)))
    b4.pack(side=LEFT, padx=5, pady=5)
    b5 = Button(root, text='Update', command = (lambda e=ents: update(e)))
    b5.pack(side=LEFT, padx=5, pady=5)
    b3 = Button(root, text='Quit', command=root.destroy)
    b3.pack(side=LEFT, padx=5, pady=5)

   
    root.mainloop()


