import ctypes

clib = ctypes.cdll.LoadLibrary('./functions.so')

print(clib.factorial(5))
