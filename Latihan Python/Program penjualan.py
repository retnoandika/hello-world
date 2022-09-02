total = 0
barang = []
harga = []

while True:
    print("""Daftar Barang\n
    1. Roti \t 5000
    2. Es Krim \t 7000
    3. Keripik \t 8000
    4. Cokelat \t 12000
    5. Buku \t 10000
    6. Pensil \t 4000
    7. Penghapus \t 3000
    """)
    
    kode = int(input("Masukkan kode barang : "))
    if kode == 1:
        barang.append('Roti')
        harga.append(5000)
        total += 5000
    elif kode == 2:
        barang.append('Es Krim')
        harga.append(7000)
        total += 7000
    elif kode == 3:
        barang.append('Keripik')
        harga.append(8000)
        total += 8000
    elif kode == 4:
        barang.append('Cokelat')
        harga.append(12000)
        total += 12000
    elif kode == 5:
        barang.append('Buku')
        harga.append(10000)
        total += 10000
    elif kode == 6:
        barang.append('Pensil')
        harga.append(4000)
        total += 4000
    else:
        print('Kode tidak valid')

    lanjut = input("Lanjut belanja?(y/t) : ")
    if lanjut == 't':
        print("")
        break

print('Barang yang dibeli : ', barang)
print('Harga barangnya : ', harga)
print('Total yang harus dibayar: ', total,'\n')

uang = int(input(f'Uang pembayaran\t: '))
if uang > total:
    print(f'kembaliannya\t: {uang - total}')
elif uang == total:
    print('Uang pas')
else:
    print(f'uang kurang\t: {uang - total}')


    