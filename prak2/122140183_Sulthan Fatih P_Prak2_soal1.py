class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def nim(self):
        return self.__nim

    @nim.setter
    def nim(self, value):
        self.__nim = value

    def method_1(self):
        return f"Method 1 dijalankan oleh {self.nama}"

    def method_2(self, parameter):
        return f"Method 2 dijalankan dengan parameter: {parameter}"

    def method_3(self):
        return f"Method 3 dijalankan oleh {self.nama} dengan NIM {self.nim}"



mahasiswa1 = Mahasiswa("122140183", "Sulthan Standing", 2022)


mahasiswa2 = Mahasiswa("122141231", "Mamank Kesbor", 2023)


print(mahasiswa1.method_1())
print(mahasiswa1.method_2("parameter"))

print(mahasiswa2.method_3())
print(mahasiswa2.method_2("parameter lain"))
