class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        print("Sebuah objek Mahasiswa telah dibuat.")
        self.__nim = nim
        self.__nama = nama
        self.__angkatan = angkatan
        self.__isMahasiswa = isMahasiswa
    
    def getNIM(self):
        return self.__nim
    
    def setNIM(self, nim):
        self.__nim = nim
    
    def getNama(self):
        return self.__nama
    
    def setNama(self, nama):
        self.__nama = nama
    
    def getAngkatan(self):
        return self.__angkatan
    
    def setAngkatan(self, angkatan):
        self.__angkatan = angkatan
    
    def getIsMahasiswa(self):
        return self.__isMahasiswa
    
    def method1(self):
        return self.__nama.upper()
    
    def method2(self):
        return f"{self.__nama} adalah mahasiswa angkatan {self.__angkatan}"
    
    def method3(self, value):
        if value > 0:
            return f"{self.__nama} memiliki nilai positif"
        else:
            return f"{self.__nama} memiliki nilai negatif"
    
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        print("Sebuah objek Mahasiswa telah dibuat.")
        self.__nim = nim
        self.__nama = nama
        self.__angkatan = angkatan
        self.__isMahasiswa = isMahasiswa
    
    def __del__(self):
        print(f"Objek Mahasiswa dengan nama {self.__nama} telah dihapus.")
        
    @staticmethod
    def info():
        return "Ini adalah kelas Mahasiswa"


mahasiswa1 = Mahasiswa("122140183", "Asep Bensin", 2022)
mahasiswa2 = Mahasiswa("081244444", "Mamank Kesbor", 2023, False)

print(mahasiswa1.method1())
print(mahasiswa1.method2())
print(mahasiswa1.method3(10))

print(mahasiswa2.method1())
print(mahasiswa2.method2())
print(mahasiswa2.method3(-5))

print(Mahasiswa.info())
