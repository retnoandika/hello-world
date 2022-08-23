# Width and Multiline
 # Data
data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

# String
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*"="+" Data String "+5*"=")
print(data_string)

# String multiline/newline/setelah enter/"\n"
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print(5*"="+" Data String "+5*"=")
print(data_string)

# String multiline (kutip triples)
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print(5*"="+" Data String "+5*"=")
print(data_string)

# mengatur lebar
data_string = f"""
nama   = {data_nama:>12}
umur   = {data_umur:>12}
tinggi = {data_tinggi:>12}
sepatu = {data_nomor_sepatu:>12}
"""
print(5*"="+" Data String "+5*"=")
print(data_string)





