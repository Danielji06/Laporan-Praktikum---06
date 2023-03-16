def persegi(tinggi, lebar):
    
    hasil = tinggi * lebar
    for i in range(hasil):
        print(i+1, end="")
        if (i+1) % lebar == 0:
            print()

tinggi = int(input("Masukkan tinggi: "))
lebar = int(input("Masukkan lebar: "))
persegi(tinggi, lebar)