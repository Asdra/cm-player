#Boa:Frame:Frame1

import wx
from ctypes import *
from buz import *
def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON10, wxID_FRAME1BUTTON11, 
 wxID_FRAME1BUTTON12, wxID_FRAME1BUTTON13, wxID_FRAME1BUTTON14, 
 wxID_FRAME1BUTTON15, wxID_FRAME1BUTTON16, wxID_FRAME1BUTTON2, 
 wxID_FRAME1BUTTON3, wxID_FRAME1BUTTON4, wxID_FRAME1BUTTON5, 
 wxID_FRAME1BUTTON6, wxID_FRAME1BUTTON7, wxID_FRAME1BUTTON8, 
 wxID_FRAME1BUTTON9, wxID_FRAME1STATICBITMAP1, wxID_FRAME1STATICBOX1, 
 wxID_FRAME1STATICLINE1, wxID_FRAME1STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(21)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(335, 147), size=wx.Size(513, 195),
              style=wx.DEFAULT_FRAME_STYLE, title='BuzSystem')
        self.SetClientSize(wx.Size(505, 168))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.SetMaxSize(wx.Size(622, 341))
        self.SetMinSize(wx.Size(0, 0))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Jouons avec la carte mere !!... || by Murf (V. Beta)',
              name='staticText1', parent=self, pos=wx.Point(8, 8),
              size=wx.Size(487, 23), style=0)
        self.staticText1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME1STATICLINE1,
              name='staticLine1', parent=self, pos=wx.Point(8, 40),
              size=wx.Size(488, 8), style=0)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label='1',
              name='button1', parent=self, pos=wx.Point(144, 72),
              size=wx.Size(24, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label='2',
              name='button2', parent=self, pos=wx.Point(184, 72),
              size=wx.Size(24, 23), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3, label='3',
              name='button3', parent=self, pos=wx.Point(224, 72),
              size=wx.Size(24, 23), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAME1BUTTON3)

        self.button4 = wx.Button(id=wxID_FRAME1BUTTON4, label='4',
              name='button4', parent=self, pos=wx.Point(264, 72),
              size=wx.Size(24, 23), style=0)
        self.button4.Bind(wx.EVT_BUTTON, self.OnButton4Button,
              id=wxID_FRAME1BUTTON4)

        self.button5 = wx.Button(id=wxID_FRAME1BUTTON5, label='5',
              name='button5', parent=self, pos=wx.Point(304, 72),
              size=wx.Size(24, 23), style=0)
        self.button5.Bind(wx.EVT_BUTTON, self.OnButton5Button,
              id=wxID_FRAME1BUTTON5)

        self.button6 = wx.Button(id=wxID_FRAME1BUTTON6, label='6',
              name='button6', parent=self, pos=wx.Point(344, 72),
              size=wx.Size(24, 23), style=0)
        self.button6.Bind(wx.EVT_BUTTON, self.OnButton6Button,
              id=wxID_FRAME1BUTTON6)

        self.button7 = wx.Button(id=wxID_FRAME1BUTTON7, label='7',
              name='button7', parent=self, pos=wx.Point(384, 72),
              size=wx.Size(24, 23), style=0)
        self.button7.Bind(wx.EVT_BUTTON, self.OnButton7Button,
              id=wxID_FRAME1BUTTON7)

        self.button8 = wx.Button(id=wxID_FRAME1BUTTON8, label='8',
              name='button8', parent=self, pos=wx.Point(424, 72),
              size=wx.Size(24, 23), style=0)
        self.button8.Bind(wx.EVT_BUTTON, self.OnButton8Button,
              id=wxID_FRAME1BUTTON8)

        self.button9 = wx.Button(id=wxID_FRAME1BUTTON9, label='9',
              name='button9', parent=self, pos=wx.Point(144, 112),
              size=wx.Size(24, 23), style=0)
        self.button9.Bind(wx.EVT_BUTTON, self.OnButton9Button,
              id=wxID_FRAME1BUTTON9)

        self.button10 = wx.Button(id=wxID_FRAME1BUTTON10, label='10',
              name='button10', parent=self, pos=wx.Point(184, 112),
              size=wx.Size(24, 23), style=0)
        self.button10.Bind(wx.EVT_BUTTON, self.OnButton10Button,
              id=wxID_FRAME1BUTTON10)

        self.button11 = wx.Button(id=wxID_FRAME1BUTTON11, label='11',
              name='button11', parent=self, pos=wx.Point(224, 112),
              size=wx.Size(24, 23), style=0)
        self.button11.Bind(wx.EVT_BUTTON, self.OnButton11Button,
              id=wxID_FRAME1BUTTON11)

        self.button12 = wx.Button(id=wxID_FRAME1BUTTON12, label='12',
              name='button12', parent=self, pos=wx.Point(264, 112),
              size=wx.Size(24, 23), style=0)
        self.button12.Bind(wx.EVT_BUTTON, self.OnButton12Button,
              id=wxID_FRAME1BUTTON12)

        self.button13 = wx.Button(id=wxID_FRAME1BUTTON13, label='13',
              name='button13', parent=self, pos=wx.Point(304, 112),
              size=wx.Size(24, 23), style=0)
        self.button13.Bind(wx.EVT_BUTTON, self.OnButton13Button,
              id=wxID_FRAME1BUTTON13)

        self.button14 = wx.Button(id=wxID_FRAME1BUTTON14, label='14',
              name='button14', parent=self, pos=wx.Point(344, 112),
              size=wx.Size(24, 23), style=0)
        self.button14.Bind(wx.EVT_BUTTON, self.OnButton14Button,
              id=wxID_FRAME1BUTTON14)

        self.button15 = wx.Button(id=wxID_FRAME1BUTTON15, label='15',
              name='button15', parent=self, pos=wx.Point(384, 112),
              size=wx.Size(24, 23), style=0)
        self.button15.Bind(wx.EVT_BUTTON, self.OnButton15Button,
              id=wxID_FRAME1BUTTON15)

        self.button16 = wx.Button(id=wxID_FRAME1BUTTON16, label='16',
              name='button16', parent=self, pos=wx.Point(424, 112),
              size=wx.Size(24, 23), style=0)
        self.button16.Bind(wx.EVT_BUTTON, self.OnButton16Button,
              id=wxID_FRAME1BUTTON16)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1, label='Sons :',
              name='staticBox1', parent=self, pos=wx.Point(128, 56),
              size=wx.Size(336, 100), style=0)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap('01.jpg',
              wx.BITMAP_TYPE_JPEG), id=wxID_FRAME1STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(8, 88),
              size=wx.Size(112, 40), style=0)
        self.staticBitmap1.SetHelpText('Double click ici = surprise')
        self.staticBitmap1.Bind(wx.EVT_LEFT_DCLICK,
              self.OnStaticBitmap1LeftDclick)

    def __init__(self, parent):
        self._init_ctrls(parent)
    
    def OnStaticBitmap1LeftDclick(self, event):
        anniv = cdll.load("sysbeuz.dll")
        anniv.birthday()
        event.Skip()
        
    def OnButton1Button(self, event):
        buz(1)
        event.Skip()

    def OnButton2Button(self, event):
        buz(2)
        event.Skip()

    def OnButton3Button(self, event):
        buz(3)
        event.Skip()

    def OnButton4Button(self, event):
        buz(4)
        event.Skip()

    def OnButton5Button(self, event):
        buz(5)
        event.Skip()

    def OnButton6Button(self, event):
        buz(6)
        event.Skip()

    def OnButton7Button(self, event):
        buz(7)
        event.Skip()

    def OnButton8Button(self, event):
        buz(8)
        event.Skip()

    def OnButton9Button(self, event):
        buz(9)
        event.Skip()

    def OnButton10Button(self, event):
        buz(10)
        event.Skip()

    def OnButton11Button(self, event):
        buz(11)
        event.Skip()

    def OnButton12Button(self, event):
        buz(12)
        event.Skip()

    def OnButton13Button(self, event):
        buz(13)
        event.Skip()

    def OnButton14Button(self, event):
        buz(14)
        event.Skip()

    def OnButton15Button(self, event):
        buz(15)
        event.Skip()

    def OnButton16Button(self, event):
        buz(16)
        event.Skip()
        
