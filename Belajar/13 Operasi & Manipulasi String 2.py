# Operator dalam bentuk methods

## merubah case dari string

# merubah semua ke upper case
salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
alay = "aKu KeCe AbieezzZZZz"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower =salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper =salam.isupper() # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() --> untuk mengecek semuanya huruf
# isalnum() --> huruf dan angka
# isdecimal() --> angka saja
# isspace() --> spasi, tab, newline \n
# istitle() --> semua kata dimulai dengan huruf besar
judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasil bool
print(judul + " is title = " + str(cek_judul))

## ngecek komponen startswith() endswith()
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppa".endswith("Oppa")
print("end = " + str(cek_end))

## panggabungan komponen join() split()
pisah =('aku','sayang','kamu')
gabungan = ','.join(pisah) # pakai koma
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah) # pakai spasi
print(gabungan)

gabungan = ' ehm '.join(pisah) # pakai spasi
print(gabungan)

gabungan = 'akuehmsayangehmkamu' # pakai spasi
print(gabungan.split('ehm'))

## alokasi karakter rjust, ljust, tengah()

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,":")
print("'"+tengah+"'")

# kebalikannya --> strip()
tengah = tengah.strip(":") # menghilangkan tanda :
print("'"+tengah+"'")




