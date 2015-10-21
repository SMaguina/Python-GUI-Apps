from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import open
from future import standard_library
standard_library.install_aliases()
import tkinter as tk
from tkinter import ttk
import webbrowser
import sqlite3

#Create database
db = sqlite3.connect('storagetest.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS content(id INTEGER PRIMARY KEY, name TEXT)''')
db.commit()

#Add entry field text into listbox
def add_item():
    listbox1.insert(tk.END, enter1.get())

#Delete listbox selection    
def delete_item():
    try:
        # get selected line index
        index = listbox1.curselection()[0]
        listbox1.delete(index)
    except IndexError:
        pass

#Bind listbox selection into entry field 
def get_list(event):
    index = listbox1.curselection()[0]
    seltext = listbox1.get(index)
    enter1.delete(0, 50)
    enter1.insert(0, seltext)

#Bind entry text into listbox    
def set_list(event):
    try:
        index = listbox1.curselection()[0]
        listbox1.delete(index)
    except IndexError:
        index = tk.END
    listbox1.insert(index, enter1.get())

#Fetch all database records to display in listbox
def sort_list():
    cont = sqlite3.connect('storagetest.db')
    with cont:
        cursort = cont.cursor()
        list_loadr = cursort.execute('''SELECT name FROM content''')
        list_load = list_loadr.fetchall()
        for item in list_load:
            listbox1.insert(tk.END, item)
            
        cont.commit()
        
#Open web browser window and display selection in HTML        
def save_list():
    f = open('index.html','w')
    text = source.get()
    message = "<html><head></head><body><p>%s</p></body></html>" % text
    f.write(message)
    f.close()
    webbrowser.open_new_tab('index.html')

root = tk.Tk()
root.title("HTML Web Page Generator")
source = tk.StringVar()


listbox1 = tk.Listbox(root, width=50, height=6)
listbox1.grid(row=0, column=0)


#Vertical scrollbar to the right of the listbox
yscroll = tk.Scrollbar(command=listbox1.yview, orient=tk.VERTICAL)
yscroll.grid(row=0, column=1, sticky=tk.N+tk.S)
listbox1.configure(yscrollcommand=yscroll.set)
 

enter1 = tk.Entry(root, textvariable=source, width=50)
enter1.insert(0, 'Click on Fetch Button, then select item in the listbox')
enter1.grid(row=1, column=0)

enter1.bind('<Return>', set_list)
enter1.bind('<Double-1>', set_list)

button1 = tk.Button(root, text='Fetch DB List    ', command=sort_list)
button1.grid(row=2, column=0, sticky=tk.W)

button2 = tk.Button(root, text='Open Browser  ', command=save_list)
button2.grid(row=3, column=0, sticky=tk.W)

button3 = tk.Button(root, text='Add entry text to listbox', command=add_item)
button3.grid(row=2, column=0, sticky=tk.E)

button4 = tk.Button(root, text='Delete selected line     ', command=delete_item)
button4.grid(row=3, column=0, sticky=tk.E)
 

listbox1.bind('<ButtonRelease-1>', get_list)
 
root.mainloop()
