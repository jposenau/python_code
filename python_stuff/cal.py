'''
Created on Jul 27, 2018

@author: jposenau
'''

import calendar, datetime, tkinter

class calendarTk(tkinter.Frame): # class calendarTk
    """ Calendar, the current date is exposed today, or transferred to date"""
    def __init__(self,master=None,date=None,dateformat="%d/%m/%Y",command=lambda i:None):
        tkinter.Frame.__init__(self, master)
        self.dt=datetime.datetime.now() if date is None else datetime.datetime.strptime(date, dateformat) 
        self.showmonth()
        self.command=command
        self.dateformat=dateformat
    def showmonth(self): # Show the calendar for a month
        sc = calendar.month(self.dt.year, self.dt.month).split('\n')
        for t,c in [('<<',0),('<',1),('>',5),('>>',6)]: # The buttons to the left to the right year and month
            tkinter.Button(self,text=t,relief='flat',command=lambda i=t:self.callback(i)).grid(row=0,column=c)
        tkinter.Label(self,text=sc[0]).grid(row=0,column=2,columnspan=3) # year and month
        for line,lineT in [(i,sc[i+1]) for i in range(1,len(sc)-1)]: # The calendar
            for col,colT in [(i,lineT[i*3:(i+1)*3-1]) for i in range(7)]: # For each element
                obj=tkinter.Button if colT.strip().isdigit() else tkinter.Label # If this number is a button, or Label
                args={'command':lambda i=colT:self.callback(i)} if obj==tkinter.Button else {} # If this button, then fasten it to the command
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

if __name__ == '__main__':
    def com(g): print ( g)
    root = tkinter.Tk()
    root.title("Monthly Calendar")
    c=calendarTk(root,date="21/11/2018",dateformat="%d/%m/%Y",command=com)
    c.pack()

    root.mainloop()