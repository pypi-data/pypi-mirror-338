#from .core1 import FractalFrame
from .algorithm.core1 import FractalFrame

__version__ = "0.2.0"  # Follow semantic versioning
__all__ = ['FractalFrame']  # Only expose Public Classes to import *
# __all__ in root __init__.py specifies what gets imported with from package import *
# Only explicitly import the public class in root __init__.py