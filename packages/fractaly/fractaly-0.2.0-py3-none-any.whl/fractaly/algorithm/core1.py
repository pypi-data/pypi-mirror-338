import wx, os, ctypes, sys
import wx.lib.colourselect as csel
import math
import random
from ..gui.core2 import _FractalCanvas
from pathlib import Path

def get_library_path():
    package_dir = Path(__file__).parent
    if sys.platform == "win32":
        return os.path.join(package_dir,"..","lib","win64","fractal_maths.dll")
    elif sys.platform == "linux":
        return os.path.join(package_dir,"..","lib","linux64","fractal_maths.so")
    else:
        raise NotImplementedError("Unsupported platform")

class FractalFrame(wx.Frame):
    def __init__(self):
        super(FractalFrame, self).__init__(None, title="Fractal Explorer", size=(800, 600))
        
        # Create the main panel
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        try:
          dll_path=get_library_path()
          print("dllPath=", dll_path)
          my_dll = ctypes.CDLL(dll_path)
          my_dll.adder.argtypes = [ctypes.c_int32, ctypes.c_int32]
          my_dll.adder.restype = ctypes.c_int32
          a=my_dll.adder(34, 12)
          if a!=46:
              print(f"error in the DLL file: 34+12={a}!")
              return 
        except:
              print ("problem in DLL loading")
              return 

        # Create the fractal canvas
        self.canvas = _FractalCanvas(panel)
        sizer.Add(self.canvas, proportion=1, flag=wx.EXPAND)
        
        # Create controls
        control_sizer = wx.GridSizer(4, 4, 5, 5)
        
        # Fractal type selector
        types = ["Mandelbrot", "Julia", "Sierpinski"]
        self.type_choice = wx.Choice(panel, choices=types)
        self.type_choice.SetSelection(0)
        self.type_choice.Bind(wx.EVT_CHOICE, self.on_type_change)
        control_sizer.Add(wx.StaticText(panel, label="Fractal Type:"), 0, wx.ALIGN_CENTER_VERTICAL)
        control_sizer.Add(self.type_choice, 0, wx.EXPAND)
        
        # Max iterations slider
        self.iter_slider = wx.Slider(panel, minValue=10, maxValue=500, value=100)
        self.iter_slider.Bind(wx.EVT_SLIDER, self.on_param_change)
        control_sizer.Add(wx.StaticText(panel, label="Max Iterations:"), 0, wx.ALIGN_CENTER_VERTICAL)
        control_sizer.Add(self.iter_slider, 0, wx.EXPAND)
        
        # Zoom slider
        self.zoom_slider = wx.Slider(panel, minValue=1, maxValue=100, value=10)
        self.zoom_slider.Bind(wx.EVT_SLIDER, self.on_zoom_change)
        control_sizer.Add(wx.StaticText(panel, label="Zoom:"), 0, wx.ALIGN_CENTER_VERTICAL)
        control_sizer.Add(self.zoom_slider, 0, wx.EXPAND)
        
        # Julia set parameter controls
        self.julia_cx = wx.Slider(panel, minValue=-200, maxValue=200, value=-70)
        self.julia_cy = wx.Slider(panel, minValue=-200, maxValue=200, value=27)
        self.julia_cx.Bind(wx.EVT_SLIDER, self.on_julia_change)
        self.julia_cy.Bind(wx.EVT_SLIDER, self.on_julia_change)
        control_sizer.Add(wx.StaticText(panel, label="Julia Cx:"), 0, wx.ALIGN_CENTER_VERTICAL)
        control_sizer.Add(self.julia_cx, 0, wx.EXPAND)
        control_sizer.Add(wx.StaticText(panel, label="Julia Cy:"), 0, wx.ALIGN_CENTER_VERTICAL)
        control_sizer.Add(self.julia_cy, 0, wx.EXPAND)
        
        # Sierpinski depth
        self.depth_slider = wx.Slider(panel, minValue=1, maxValue=10, value=5)
        self.depth_slider.Bind(wx.EVT_SLIDER, self.on_param_change)
        control_sizer.Add(wx.StaticText(panel, label="Sierpinski Depth:"), 0, wx.ALIGN_CENTER_VERTICAL)
        control_sizer.Add(self.depth_slider, 0, wx.EXPAND)
        
        # Color selector
        self.color_btn = csel.ColourSelect(panel, colour=wx.RED, size=(30, 20))
        self.color_btn.Bind(csel.EVT_COLOURSELECT, self.on_color_change)
        control_sizer.Add(wx.StaticText(panel, label="Color Scheme:"), 0, wx.ALIGN_CENTER_VERTICAL)
        control_sizer.Add(self.color_btn, 0, wx.EXPAND)
        
        # Reset view button
        reset_btn = wx.Button(panel, label="Reset View")
        reset_btn.Bind(wx.EVT_BUTTON, self.on_reset_view)
        control_sizer.Add(reset_btn, 0, wx.EXPAND)
        
        # Randomize button
        random_btn = wx.Button(panel, label="Randomize")
        random_btn.Bind(wx.EVT_BUTTON, self.on_randomize)
        control_sizer.Add(random_btn, 0, wx.EXPAND)
        
        sizer.Add(control_sizer, flag=wx.EXPAND|wx.ALL, border=5)
        panel.SetSizer(sizer)
        
        # Bind mouse events for zooming and panning
        self.canvas.Bind(wx.EVT_LEFT_DOWN, self.on_mouse_down)
        self.canvas.Bind(wx.EVT_MOTION, self.on_mouse_move)
        self.canvas.Bind(wx.EVT_MOUSEWHEEL, self.on_mouse_wheel)
        
        self.update_controls()
    
    def update_controls(self):
        fractal_type = self.canvas.fractal_type
        self.julia_cx.Enable(fractal_type == "Julia")
        self.julia_cy.Enable(fractal_type == "Julia")
        self.depth_slider.Enable(fractal_type == "Sierpinski")
        
        self.iter_slider.SetValue(self.canvas.max_iter)
        self.zoom_slider.SetValue(int(self.canvas.zoom * 10))
        self.julia_cx.SetValue(int(self.canvas.julia_c[0] * 100))
        self.julia_cy.SetValue(int(self.canvas.julia_c[1] * 100))
        self.depth_slider.SetValue(self.canvas.sierpinski_depth)
    
    def on_type_change(self, event):
        self.canvas.fractal_type = self.type_choice.GetStringSelection()
        self.update_controls()
        self.canvas.generate_fractal()
    
    def on_param_change(self, event):
        self.canvas.max_iter = self.iter_slider.GetValue()
        self.canvas.sierpinski_depth = self.depth_slider.GetValue()
        self.canvas.generate_fractal()
    
    def on_zoom_change(self, event):
        self.canvas.zoom = self.zoom_slider.GetValue() / 10.0
        self.canvas.generate_fractal()
    
    def on_julia_change(self, event):
        self.canvas.julia_c = (self.julia_cx.GetValue() / 100.0, 
                              self.julia_cy.GetValue() / 100.0)
        self.canvas.generate_fractal()
    
    def on_color_change(self, event):
        # Simple color scheme - you could expand this to use multiple colors
        base_color = self.color_btn.GetColour()
        r, g, b = base_color.Red(), base_color.Green(), base_color.Blue()
        self.canvas.color_scheme = [
            (0, 0, 0),
            (r, g, b),
            (min(r+100, 255), min(g+100, 255), min(b+100, 255)),
            (255, 255, 255)
        ]
        self.canvas.generate_fractal()
    
    def on_reset_view(self, event):
        self.canvas.zoom = 1.0
        self.canvas.pan_x, self.canvas.pan_y = 0.0, 0.0
        self.zoom_slider.SetValue(10)
        self.canvas.generate_fractal()
    
    def on_randomize(self, event):
        if self.canvas.fractal_type == "Julia":
            self.julia_cx.SetValue(random.randint(-200, 200))
            self.julia_cy.SetValue(random.randint(-200, 200))
            self.on_julia_change(None)
        else:
            self.color_btn.SetColour(wx.Colour(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            ))
            self.on_color_change(None)
    
    def on_mouse_down(self, event):
        self.last_mouse_pos = event.GetPosition()
        event.Skip()
    
    def on_mouse_move(self, event):
        if event.Dragging() and event.LeftIsDown():
            x, y = event.GetPosition()
            dx = x - self.last_mouse_pos.x
            dy = y - self.last_mouse_pos.y
            
            # Adjust pan based on mouse movement
            self.canvas.pan_x -= dx * 0.005 / self.canvas.zoom
            self.canvas.pan_y -= dy * 0.005 / self.canvas.zoom
            
            self.last_mouse_pos = event.GetPosition()
            self.canvas.generate_fractal()
        event.Skip()
    
    def on_mouse_wheel(self, event):
        # Zoom in/out based on wheel rotation
        rotation = event.GetWheelRotation()
        zoom_factor = 1.2 if rotation > 0 else 1/1.2
        
        self.canvas.zoom *= zoom_factor
        self.zoom_slider.SetValue(int(self.canvas.zoom * 10))
        self.canvas.generate_fractal()

#if __name__ == "__main__":
 #   app = wx.App(False)
  #  frame = FractalFrame()
   # frame.Show()
   # app.MainLoop()