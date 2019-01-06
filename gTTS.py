import wx
import wx.grid
import speech
import readMail


class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(617, 329), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"gTTS Gmail Access", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_CENTRE)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(wx.Font(16, 72, 93, 90, False, wx.EmptyString))

        bSizer2.Add(self.m_staticText3, 0, wx.ALL, 5)

        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_grid1 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid1.CreateGrid(5, 1)
        self.m_grid1.EnableEditing(True)
        self.m_grid1.EnableGridLines(True)
        self.m_grid1.EnableDragGridSize(False)
        self.m_grid1.SetMargins(0, 0)

        # Columns
        self.m_grid1.SetColSize(0, 250)
        self.m_grid1.EnableDragColMove(False)
        self.m_grid1.EnableDragColSize(True)
        self.m_grid1.SetColLabelSize(30)
        self.m_grid1.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid1.EnableDragRowSize(True)
        self.m_grid1.SetRowLabelSize(50)
        self.m_grid1.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        fgSizer1.Add(self.m_grid1, 0, wx.ALL, 5)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.m_textCtrl2 = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.m_textCtrl2.SetMinSize(wx.Size(250, 200))

        sbSizer1.Add(self.m_textCtrl2, 0, wx.ALL, 5)

        self.m_button1 = wx.Button(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Play", wx.Point(-1, -1), wx.DefaultSize, 0)
        sbSizer1.Add(self.m_button1, 0, wx.ALL, 5)

        fgSizer1.Add(sbSizer1, 1, wx.EXPAND, 5)

        bSizer2.Add(fgSizer1, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # declaration
        self.m_button1.Bind(wx.EVT_BUTTON, self.btn_speech)

    def __del__(self):
        pass

    @staticmethod
    def btn_speech(event):
        status = readMail.save_speech()
        if status == 0:
            speech.dari()
            speech.subjek()
            speech.speech()
            # wx.MessageBox('', 'Sukses', wx.OK)
        else:
            wx.MessageBox('', 'Failed', wx.OK)


class MainApp(wx.App):
    def OnInit(self):
        mainFrame = MyFrame1(None)
        mainFrame.Show(True)
        return True


if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()
