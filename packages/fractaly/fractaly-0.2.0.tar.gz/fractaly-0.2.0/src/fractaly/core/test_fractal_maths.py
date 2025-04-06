import ctypes
import os

# Load the DLL
my_dll = ctypes.CDLL(os.path.abspath('fractal_maths.dll'))

# Specify the argument and return types
my_dll.adder.argtypes = [ctypes.c_int32, ctypes.c_int32]
my_dll.adder.restype = ctypes.c_int32

# Define a Python wrapper function
def adder(a, b) :
    return my_dll.adder(a, b)

    # Test the function
if __name__ == "__main__":
  num1 = 10
  num2 = 20
  result = adder(num1, num2)
  print(f"{num1} + {num2} = {result}")