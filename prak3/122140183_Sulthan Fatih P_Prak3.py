# Nama : Sulthan Fatih P
# NIM  : 122140183

class dagangan : 
    jumlah_barang = 0
    list_barang = []

    def _init_(self, nama, harga, stok):
        self.nama = nama
        self.__harga = harga
        self.stok = stok
        dagangan.jumlah_barang += 1
        dagangan.list_barang.append((self.nama, self.__harga, self.stok))

    def lihat_barang(self):
        print(f"jumlah barang dagangan pada toko : {dagangan.jumlah_barang} buah")
        for i in range(len(dagangan.list_barang)):
            print(f"{i+1}. {dagangan.list_barang[i][0]} seharga Rp {dagangan.list_barang[i][2]} (stok: {dagangan.list_barang[i][1]})")
    
    def _del_(self):
        index = dagangan.list_barang.index((self.nama, self.__harga, self.stok))
        del dagangan.list_barang[index]
        dagangan.jumlah_barang -= 1
        print(f"{self.nama} dihapus dari toko!")


barang1 = dagangan("Galon Aqua 19L", 32, 17000)
barang2 = dagangan("Gas LPG 5 kg", 22, 88000)
barang3 = dagangan("Beras Ramos 5 kg", 13, 68000)
barang1.lihat_barang()
del barang1
barang2.lihat_barang()