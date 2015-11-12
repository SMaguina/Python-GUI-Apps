import wx

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None,\
          title=title, size=(300,250))
        panel = wx.Panel(self)
        button = wx.Button(panel,label="Exit",size=(100,40),pos=(100,100))
        # Bind button event to the function self.exit
        button.Bind(wx.EVT_BUTTON, self.exit)

        # Create menu bar
        menuBar = wx.MenuBar()
        # Create wx menus
        fileMenu = wx.Menu()
        editMenu = wx.Menu()

        # Add items to fileMenu
        fileMenu.Append(wx.NewId(), "New File", "Create a new file")
        fileMenu.Append(wx.NewId(), "Open")
        exitItem = fileMenu.Append(wx.NewId(), "Exit")
        editMenu.Append(wx.NewId(), "Undo")
        editMenu.Append(wx.NewId(), "Redo")

        # Bind exit menu item to exit function
        self.Bind(wx.EVT_MENU, self.exit, exitItem)

        # Add fileMenu and editMenu to menuBar
        menuBar.Append(fileMenu, "File")
        menuBar.Append(editMenu, "Edit")
        
        self.SetMenuBar(menuBar)

        self.CreateStatusBar()

        sc = wx.SpinCtrl(panel, value='0', pos=(100, 50), size=(70, 25))
        self.valueText = wx.StaticText(panel, label='', pos=(130,80))

        sc.Bind(wx.EVT_SPINCTRL, self.spinControl)

    def spinControl(self, event):
        # Get spin control value
        value = event.GetPosition()
        # Update static text
        self.valueText.SetLabel(str(value))
    
    def exit(self, event):
        self.Destroy()

app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()
