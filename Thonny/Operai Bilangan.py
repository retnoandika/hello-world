def MenuUtama():
    isi='''
    1. Perkalian
    2. Penjumlahan
    3. Pengurangan
    4. Bilangan Bulat
    5. Bilangan Prima
    6. Bilangan Pecahan
    7. Keluar
'''

    print(isi)
    pilihan = input("Masukkan pilihan dalam angka 1-7: ")
    if pilihan == "1":
        Perkalian()
    elif pilihan == "2":
        Penjumlahan()
    elif pilihan == "3":
        Pengurangan()
    elif pilihan == "4":
        Bilangan_Bulat()
    elif pilihan == "5":
        Bilangan_Prima()
    elif pilihan == "6":
        Bilangan_Pecahan()
    elif pilihan == "7":
        print("Terima Kasih")
    else :
        MenuUtama()

def Perkalian():
    print("Modul Perkalian")
    bilangan1 = int(input("Masukkan Bilangan 1 = "))
    bilangan2 = int(input("Masukkan Bilangan 2 = "))
    hasil = bilangan1 * bilangan2
    print(bilangan1, "x", bilangan2, "=", hasil)
    MenuUtama()

def Penjumlahan():
    print("Modul Penjumlahan")
    bilangan1 = int(input("Masukkan Bilangan 1 = "))
    bilangan2 = int(input("Masukkan Bilangan 2 = "))
    hasil = bilangan1 + bilangan2
    print("Hasil Penjumlahan", bilangan1, "+", bilangan2, "=", hasil)
    MenuUtama()

def Pengurangan():
    print("Modul Pengurangan")
    bilangan1 = int(input("Masukkan Bilangan 1 = "))
    bilangan2 = int(input("Masukkan Bilangan 2 = "))
    hasil = bilangan1 - bilangan2
    print("Hasil Pengurangan", bilangan1, "-", bilangan2, "=", hasil)
    MenuUtama()
    
def Bilangan_Bulat():
    print("Modul Bilangan Bulat")
    bilangan = float(input("Masukkan bilangan: "))
    bilangan_bulat = bilangan.is_integer()

    if bilangan_bulat:
        print(bilangan, "adalah bilangan bulat")
    else:
        print(bilangan, "bukan bilangan bulat")
    MenuUtama()

def Bilangan_Prima():
    print("Modul Bilangan Prima")
    n = int(input())
    prima = ("Termasuk Bilangan Prima")
    for i in range (2,n):
        if(n % i == 0):
            prima = ("Bukan Termasuk Bilangan Prima")
    print(prima)
    MenuUtama()
    
def Bilangan_Pecahan():
    print("Modul Bilangan Pecahan")
    bilangan = float(input("Masukkan bilangan: "))
    bilangan_pecahan = bilangan.is_integer()

    if bilangan_pecahan:
        print(bilangan, "bukan bilangan pecahan")
    else:
        print(bilangan, "adalah bilangan pecahan")
    MenuUtama()

MenuUtama()


