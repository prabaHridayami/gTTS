import wx
import speech
import readMail


class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"Play", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.m_button1, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.m_button2, 0, wx.ALL, 5)

        self.SetSizer(fgSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # declaration
        self.m_button1.Bind(wx.EVT_BUTTON, self.btn_speech)
        self.m_button2.Bind(wx.EVT_BUTTON, self.btn_save)

    def __del__(self):
        pass

    def btn_speech(self, event):
        speech.speech()
        # wx.MessageBox('', 'Sukses', wx.OK)

    def btn_save(self, event):
        readMail.save_speech()
        wx.MessageBox('Save Succes', 'Sukses', wx.OK)




class MainApp(wx.App):
    def OnInit(self):
        mainFrame = MyFrame1(None)
        mainFrame.Show(True)
        return True


if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()
