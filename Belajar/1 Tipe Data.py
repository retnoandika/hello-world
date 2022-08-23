# integer
data_integer = 1
print("data: ", data_integer) 
print("- bertipe: ", type(data_integer))

# float
data_float = 1.5
print("data: ", data_float) 
print("- bertipe: ", type(data_float))

# string
data_string = "Retno"
print("data: ", data_string) 
print("- bertipe: ", type(data_string))

# boolean
data_bool = True
print("data: ", data_bool) 
print("- bertipe: ", type(data_bool))

# bilangan kompleks
data_complex = complex(5,6)
print("data: ", data_complex) 
print("- bertipe: ", type(data_complex))

# dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("data: ", data_c_double) 
print("- bertipe: ", type(data_c_double))
