def deret_segitiga(n):
    for i in range(n, 0, -1):
        temp = 1
        
        for j in range(i, i+1):
            temp = temp * j
            print(temp, end="")

            for j in range(i, 0, -1):
                print(j, end="")
            print()

n = int(input("Masukkan n: "))
deret_segitiga(n)