

a = int(input("Inputkan batas bawah : "))
b = int(input("Inputkan batas atas : "))
c = 0

if(a < 0 or b < 0 ):
    print("Batas bawah dan atas tidak boleh dibawah nol")
else:
    for i in range (a,b):
        if(i%2 == 1):
            print(i)
            c += i
    print("Jumlah total bilangan ganjil adalah = " + str(c))
        

