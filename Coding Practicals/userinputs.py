import wx

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

        #Name Pop up box
        nameBox = wx.TextEntryDialog(None, 'What is your name?', 'Welcome','name')

        if nameBox.ShowModal()==wx.ID_OK:
            userName = nameBox.GetValue()
        
        #Question Pop up box
        yesNoBox = wx.MessageDialog(None, 'Do you enjoy wxPython?','Question',wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()

        if yesNoAnswer == wx.ID_NO:
            userName = 'Loser!'

        #Multiple choice input
        chooseOneBox = wx.SingleChoiceDialog(None, 'What is your favorite color?',
                                             'Color Question',
                                             ['Green','Red','Blue','Yellow'])

        if chooseOneBox.ShowModal() == wx.ID_OK:
            favColor = chooseOneBox.GetStringSelection()

        #Creates text box panel
        wx.TextCtrl(panel, pos=(3, 100), size=(150,50))

        #Text
        aweText = wx.StaticText(panel, -1, "Awesome Text", (3,3))
        aweText.SetForegroundColour('yellow')
        aweText.SetBackgroundColour('black')

        rlyAweText = wx.StaticText(panel, -1, "Customized Awesomeness",(3,30))
        rlyAweText.SetForegroundColour(favColor)
        rlyAweText.SetBackgroundColour('black')

        self.SetTitle('Welcome '+userName)

        self.Show(True)

    def Quit(self, e):
        self.Close()
        
        
app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()
