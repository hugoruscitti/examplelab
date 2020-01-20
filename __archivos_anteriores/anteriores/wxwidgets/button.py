import wx

class ExampleFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent)

        self.quote = wx.StaticText(self, label="Your quote :", pos=(20, 30), size=(200, -1))
        clearButton = wx.Button(self, wx.ID_CLEAR, "Clear")
        self.Bind(wx.EVT_BUTTON, self.on_clean_clicked, clearButton)

        self.Show()


    def on_clean_clicked(self, event):
        print "Se ha pulsado el boton de limpiar."

app = wx.App(False)
ExampleFrame(None)
app.MainLoop()
