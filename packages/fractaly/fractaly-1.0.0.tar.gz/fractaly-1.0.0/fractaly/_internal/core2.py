import wx
import time

class _FractalCanvas(wx.Panel):
    def __init__(self, parent):
        super(_FractalCanvas, self).__init__(parent)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_SIZE, self.on_size)
        
        # Fractal parameters
        self.sierpinski_depth = 5
        self.fractal_type = "Mandelbrot"
        self.max_iter = 100
        self.color_scheme = [(0, 0, 0), (255, 0, 0), (255, 255, 0), (0, 0, 255)]
        self.julia_c = (-0.7, 0.27)


        # View parameters
        self.zoom = 1.0
        self.pan_x, self.pan_y = 0.0, 0.0
        self.last_draw_time = 0
        
        # Generate initial fractal
        self.generate_fractal()
    
    def generate_fractal(self):
        start_time = time.time()
        width, height = self.GetClientSize()
        
        if width <= 0 or height <= 0:
            return
            
        # Create a bitmap to draw on
        self.bmp = wx.Bitmap(width, height)
        dc = wx.MemoryDC(self.bmp)
        dc.Clear()
        
        if self.fractal_type == "Mandelbrot":
            self.draw_mandelbrot(dc, width, height)
        elif self.fractal_type == "Julia":
            self.draw_julia(dc, width, height)
        elif self.fractal_type == "Sierpinski":
            self.draw_sierpinski(dc, width, height)
        
        del dc  # Release the DC
        self.last_draw_time = time.time() - start_time
        self.Refresh()
    
    def draw_mandelbrot(self, dc, width, height):
        for x in range(width):
            for y in range(height):
                # Convert pixel coordinates to complex numbers
                zx = 1.5 * (x - width / 2) / (0.5 * self.zoom * width) + self.pan_x
                zy = (y - height / 2) / (0.5 * self.zoom * height) + self.pan_y
                
                c = zx + zy * 1j
                z = 0 + 0j
                iter = 0
                
                while abs(z) < 2 and iter < self.max_iter:
                    z = z * z + c
                    iter += 1
                
                color = self.get_color(iter)
                dc.SetPen(wx.Pen(color))
                dc.DrawPoint(x, y)
    
    def draw_julia(self, dc, width, height):
        cx, cy = self.julia_c
        c = cx + cy * 1j
        
        for x in range(width):
            for y in range(height):
                # Convert pixel coordinates to complex numbers
                zx = 1.5 * (x - width / 2) / (0.5 * self.zoom * width) + self.pan_x
                zy = (y - height / 2) / (0.5 * self.zoom * height) + self.pan_y
                
                z = zx + zy * 1j
                iter = 0
                
                while abs(z) < 2 and iter < self.max_iter:
                    z = z * z + c
                    iter += 1
                
                color = self.get_color(iter)
                dc.SetPen(wx.Pen(color))
                dc.DrawPoint(x, y)
    
    def draw_sierpinski(self, dc, width, height):
        dc.SetBackground(wx.Brush(wx.WHITE))
        dc.Clear()
        
        size = int(min(width, height) * 0.9)
        x_offset = int((width - size) / 2)
        y_offset = int((height - size) / 2)
        
        # Define the initial triangle points
        triangle = [
            (int(x_offset + size / 2), y_offset),
            (x_offset, y_offset + size),
            (x_offset + size, y_offset + size)
        ]
        
        self.draw_sierpinski_recursive(dc, triangle, self.sierpinski_depth)
    
    def draw_sierpinski_recursive(self, dc, triangle, depth):
        if depth == 0:
            dc.SetPen(wx.Pen(wx.BLACK, 1))
            dc.DrawPolygon(triangle)  # Draw the filled triangle
            return
        
        # Calculate midpoints
        a, b, c = triangle
        ab = (int((a[0] + b[0]) / 2), int((a[1] + b[1]) / 2))
        ac = (int((a[0] + c[0]) / 2),int( (a[1] + c[1]) / 2))
        bc = (int((b[0] + c[0]) / 2), int((b[1] + c[1]) / 2))
        
        # Draw three smaller triangles
        self.draw_sierpinski_recursive(dc, [a, ab, ac], depth - 1)
        self.draw_sierpinski_recursive(dc, [ab, b, bc], depth - 1)
        self.draw_sierpinski_recursive(dc, [ac, bc, c], depth - 1)
    
    def get_color(self, iter):
        if iter == self.max_iter:
            return wx.Colour(0, 0, 0)  # Black for points in the set
        # Smooth coloring
        t = iter / self.max_iter
        idx = int(t * (len(self.color_scheme) - 1))
        t = t * (len(self.color_scheme) - 1) - idx
        
        if idx >= len(self.color_scheme) - 1:
            return wx.Colour(*self.color_scheme[-1])
        
        r = int(self.color_scheme[idx][0] + t * (self.color_scheme[idx+1][0] - self.color_scheme[idx][0]))
        g = int(self.color_scheme[idx][1] + t * (self.color_scheme[idx+1][1] - self.color_scheme[idx][1]))
        b = int(self.color_scheme[idx][2] + t * (self.color_scheme[idx+1][2] - self.color_scheme[idx][2]))
        
        return wx.Colour(r, g, b)
    
    def on_paint(self, event):
        dc = wx.BufferedPaintDC(self)
        if hasattr(self, 'bmp'):
            dc.DrawBitmap(self.bmp, 0, 0)
        
        # Display rendering time
        dc.SetTextForeground(wx.WHITE)
        dc.SetBackgroundMode(wx.SOLID)
        dc.SetBackground(wx.Brush(wx.BLACK))
        dc.DrawText(f"Render time: {self.last_draw_time:.2f}s", 10, 10)
    
    def on_size(self, event):
        self.generate_fractal()
        event.Skip()
 