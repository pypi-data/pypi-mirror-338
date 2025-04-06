#package entry point
import wx
from  .algorithm.core1 import FractalFrame

if __name__ == "__main__":
  app = wx.App(False)
  frame = FractalFrame()
  frame.Show()
  app.MainLoop()
