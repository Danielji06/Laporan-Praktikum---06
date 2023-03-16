def mencari_bilangan_prima(angka):
    if angka <= 2:
        return False
    for i in range(n-1, 2, -1):
        if i % 2 != 0:
            for j in range(3, i):
                if i % j == 0:
                    break
                else:
                    if j == i-1:    
                        return i
    return 2

print(mencari_bilangan_prima(3))