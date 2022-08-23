# Merubah dari satu tipe ke tipe lain

# Integer
print("=============Integer=============")
data_int = 9;
print("data =", data_int, ",type =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data =", data_float, ",type =", type(data_float))
print("data =", data_str, ",type =", type(data_str))
print("data =", data_bool, ",type =", type(data_bool))

# Float
print("=============Float=============")
data_float = 0;
print("data =", data_float, ",type =", type(data_float))

data_int = int(data_float) # hasilnya akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)
print("data =", data_int, ",type =", type(data_int))
print("data =", data_str, ",type =", type(data_str))
print("data =", data_bool, ",type =", type(data_bool))

# Boolean
print("=============Boolean=============")
data_bool = True;
print("data =", data_bool, ",type =", type(data_bool))

data_int = int(data_bool) 
data_str = str(data_bool)
data_float = float(data_bool)
print("data =", data_int, ",type =", type(data_int))
print("data =", data_str, ",type =", type(data_str))
print("data =", data_float, ",type =", type(data_float))

# String
print("=============String=============")
data_str = "10";
print("data =", data_str, ",type =", type(data_str))

#data_int = int(data_str) # str harus angka
data_bool = bool(data_str) # str harus angka
data_float = float(data_str) # false jika str kosong
print("data =", data_int, ",type =", type(data_int))
print("data =", data_bool, ",type =", type(data_bool))
print("data =", data_float, ",type =", type(data_float))














