#written in Python 3
import wx
import sqlite3
import os
import datetime as dt
import time
import shutil
        
class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(500,250))

        panel = wx.Panel(self)
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()

        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Quit\tCtrl+P')

        #Create wx menus
        fileMenu = wx.Menu()
        editMenu = wx.Menu()

        #Add items to fileMenu
        fileMenu.Append(wx.NewId(), "New File", "Create a new file")
        fileMenu.Append(wx.NewId(), "Open")
        exitItem = fileMenu.Append(wx.NewId(), "Exit")
        editMenu.Append(wx.NewId(), "Undo")
        editMenu.Append(wx.NewId(), "Redo")

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)

        menuBar.Append(fileMenu, "File")
        menuBar.Append(editMenu, "Edit")

        #Step 1: Browse and Choose Files to be checked daily
        directory = wx.DirSelector("Choose the folder that is checked daily")

        if not directory.strip():
            # User cancelled the dialog...
            self.exit()

        #Step 2: Browse and Choose folder to receive copied files
        directory = wx.DirSelector("Choose a folder to receive the copied files")

        if not directory.strip():
            # User cancelled the dialog...
            self.exit()
        
        #Step 3: Question Pop up box
        yesNoBox = wx.MessageDialog(None, 'Would you like to run a file check?','Permission to Run',wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()
        
        confirmText = wx.StaticText(panel, -1, "File Check Complete!", (3,3))

        #Step 4: Displays last file check date/time in GUI
        now = wx.DateTime.Now()
        timecheckText = wx.StaticText(panel, -1, "Last file check done:\t%s\n"%(now.Format("%c", wx.DateTime.PST)), (3,30))

        self.SetTitle('Welcome')

        self.Show(True)

        #Create and connect to database
        conn = sqlite3.connect('record.db')

        c = conn.cursor()

        #Create table named FILE_CHECK for File Check Process record
        conn.execute("CREATE TABLE if not exists FILE_CHECK( ID INTEGER, datestamp TEXT );")

        idfordb = 1
        date = str(dt.datetime.fromtimestamp(int(time.time())).strftime('%Y-%M-%D %H:%M:%S'))

        #Records data/time stamp into FILE_CHECK table
        c.execute("INSERT INTO FILE_CHECK(ID, datestamp) VALUES(?,?)", (idfordb, date))

        conn.commit()

        for root,dirs,files in os.walk('/Users/Sylvia/Desktop/EdittedFolder'):

            for item in files:
                now = dt.datetime.now()
                yesterday = now - dt.timedelta(days=1)
                path = os.path.join(root,item)
                st = os.stat(path)

        mod_time = dt.datetime.fromtimestamp(st.st_ctime)
        if mod_time < yesterday:
            shutil.move(os.path.join(root,item), '/Users/Sylvia/Desktop/HomeOffice')
            print('Files created or modified yesterday have been transferred')
        else:
            print(('%s last modified %s'%(path,mod_time)))

    def Quit(self, e):
        self.Close()
        
        
app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()
