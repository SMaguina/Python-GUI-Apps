from tkinter import *
from tkinter import ttk
import webbrowser
import sqlite3

#Create database
db = sqlite3.connect('storagetest.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS content(id INTEGER PRIMARY KEY, name TEXT)''')
db.commit()

wbGui = Tk()
source = StringVar()

#Add record entry into listbox and database
def addRecord():
    name_i = source.get()
    con = sqlite3.connect('storagetest.db')
    with con:
        cursor = con.cursor()
        cursor.execute('''INSERT INTO content(name) VALUES(?)''', (name_i,))
        lis = cursor.execute('''SELECT name FROM content''')
        for item in lis:
            list.insert(END, item)

        con.commit()
    print("Record added")
    con.close()

#Fetch all database records to display in listbox
def fetchRecord():
    cont = sqlite3.connect('storagetest.db')
    with cont:
        cursort = cont.cursor()
        list_loadr = cursort.execute('''SELECT name FROM content''')
        list_load = list_loadr.fetchall()
        for item in list_load:
            list.insert(END, item)
            
        cont.commit()
        
#Load is supposed to select content choice and insert into text field
def loadRecord():
    name_i = source.get()
    cont = sqlite3.connect('storagetest.db')
    c = cont.cursor()
    c.execute('SELECT * FROM content')
    for item in c:
        list.get(list.curselection())
    cont.commit()
    print ("select")
        
#Open web browser window and display selection in HTML
def wbbrowser():
    f = open('index.html','w')
    text = source.get()
    message = "<html><head></head><body><p>%s</p></body></html>" % text
    f.write(message)
    f.close()
    webbrowser.open_new_tab('index.html')
    
        
wbGui.geometry('450x450+500+300')
wbGui.title('Web Browser')
wblabel = Label(wbGui,text='Type Your Text Below').pack()
wbEntry = ttk.Entry(wbGui,textvariable=source).pack()

#Row of buttons
frame2 = Frame(wbGui)
frame2.pack()
wbbutton1 = Button(frame2,text="Add",command = addRecord)
wbbutton2 = Button(frame2,text="Load",command = loadRecord)
wbbutton3 = Button(frame2,text="Fetch",command = fetchRecord)
wbbutton4 = Button(frame2,text="Open Browser",command = wbbrowser)
wbbutton1.pack(side=LEFT); wbbutton2.pack(side=LEFT)
wbbutton3.pack(side=LEFT); wbbutton4.pack(side=LEFT)

list = Listbox(wbGui)


list.pack()
wbGui.mainloop()
