import wx
import os
import datetime as dt
import shutil

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(300,250))

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

        #Creates text box panel
        wx.TextCtrl(panel, pos=(3, 100), size=(150,50))

        #Text
        aweText = wx.StaticText(panel, -1, "File Check Complete!", (3,3))

        self.SetTitle('Welcome')

        self.Show(True)

    def Quit(self, e):
        self.Close()
        
        
app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()

for root,dirs,files in os.walk('/Users/Sylvia/Desktop/EdittedFolder'):

    for item in files:
        now = dt.datetime.now()
        yesterday = now - dt.timedelta(hours=24)
        path = os.path.join(root,item)
        st = os.stat(path)

    mod_time = dt.datetime.fromtimestamp(st.st_ctime)
    if mod_time < yesterday:
        shutil.move(os.path.join(root,item), '/Users/Sylvia/Desktop/HomeOffice')
        print('Files created or modified yesterday have been transferred')
    else:
        print('%s last modified %s'%(path,mod_time))
