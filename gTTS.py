import wx
import wx.grid
import speech
import readMail


class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(723, 473), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"gTTS Read Gmail Message", wx.DefaultPosition,
                                           wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(wx.Font(16, 72, 93, 90, False, wx.EmptyString))

        bSizer2.Add(self.m_staticText3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.m_button1 = wx.Button(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Play", wx.Point(-1, -1), wx.DefaultSize, 0)
        sbSizer1.Add(self.m_button1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Dari", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        sbSizer1.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_text1 = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.Size(800, -1), 0)
        sbSizer1.Add(self.m_text1, 0, wx.ALL, 5)

        self.m_staticText31 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Subjek", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        sbSizer1.Add(self.m_staticText31, 0, wx.ALL, 5)

        self.m_text2 = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.Size(800, -1), 0)
        sbSizer1.Add(self.m_text2, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Pesan", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        sbSizer1.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_text3 = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        self.m_text3.SetMinSize(wx.Size(800, 200))

        sbSizer1.Add(self.m_text3, 0, wx.ALL, 5)

        bSizer2.Add(sbSizer1, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # declaration
        self.m_button1.Bind(wx.EVT_BUTTON, self.btn_speech)

    def __del__(self):
        pass

    def btn_speech(self,event):
        #menjalankan fungsi save_speech pada file readMail.py
        status = readMail.save_speech(self)
        #jika status yang dikembalikan 0 maka fungsi-fungsi dari file speech dijalankan
        if status == 0:
            speech.dari()
            speech.subjek()
            speech.speech()
        else:
            #jika tidak maka akan menampilkan messageBox bahwa semua pesan telah terbaca
            wx.MessageBox('Semua email telah terbaca', 'Message', wx.OK)


class MainApp(wx.App):
    def OnInit(self):
        mainFrame = MyFrame1(None)
        mainFrame.Show(True)
        return True


if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()
