# Fractaly - Fractal Visualization Tool

![Fractal Example](docs/images/mandelbrot.png)

A cross-platform application for generating and exploring fractal images.

## Features
- Multiple fractal types (Mandelbrot, Julia, etc.)
- Interactive zoom/pan
- Custom color schemes

## Installation
```bash
pip install -e . 
```

## Usage
```python
import wx
import fractaly
app = wx.App(False)
frame = fractaly.FractalFrame()
frame.Show()
app.MainLoop()
```