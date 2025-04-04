import wx
import fractaly
 
#if __name__ == "__main__":
app = wx.App(False)
frame = fractaly.FractalFrame()
frame.Show()
app.MainLoop()