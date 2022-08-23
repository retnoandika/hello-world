data = 'ini adalah string'
print(data)
print(type(data))

# 1. Cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote '...'
'''
data = 'Menggunakan single quote'
print(data)

data = 'Menggunakan double quote'
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")

# 2. Menggunakan tanda \
# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day isn\t it?')

# backlash
print("C:\\user\\Retno")

# tab
print("Retno\t\t\tolong, semakin jauh")

# backspace
print("Retno \btolong, jadi dekatan")

# newline
print("baris pertama.\nbaris kedua.") # LF -> line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") # CR -> carriage return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return -> windows

# 3. String literal atau raw
# hati-hati
print('C:\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Retno
Kelas : 2 AK
""")

# multiline literal string dan raw
print(r"""
Nama : Retno 
Kelas : 2 AK\new normal
Website : www.retno.com/newID
""")


