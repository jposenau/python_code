import tkinter as tk

class Demo1:
    def __init__(self, root):
        ents = makeform(root, fields)
    #    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
        b1 = self.Button(root, text='Show',
            command=(lambda e=ents: fetch(e)))
        b1.pack(side=tk.LEFT, padx=5, pady=5) 
        b2 = self.Button(root, text='Enter', command = (lambda e=ents: entry(e)))
        b2.pack(side=tk.LEFT, padx=5, pady=5)
        b4 = self.Button(root, text = 'List', command = (lambda e=ents: list_books(root)))
        b4.pack(side=tk.LEFT, padx=5, pady=5)
        b3 = self.Button(root, text='Quit', command=root.quit)
        b3.pack(side=tk.LEFT, padx=5, pady=5)

    def get_connection(self):
        global _connection
        if not _connection:
            _connection = mysql.connector.connect(user='jposenau',
            database='mine',
            password = 'Dadrules503',
            host = '127.0.0.1' )
            return _connection        
    def fetch(self,entries):
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

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()