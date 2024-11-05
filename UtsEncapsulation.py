class Perpustakaan:
    def __init__(self):
        self.__koleksiBuku = "Ini adalah koleksi buku privat di perpustakaan"

    # metode privat
    def __infoKoleksiBuku(self):
        return "Ini adalah metode privat untuk informasi koleksi buku"

    # getter
    def getKoleksiBuku(self):
        return self.__koleksiBuku

    # setter
    def setKoleksiBuku(self, koleksiBaru):
        self.__koleksiBuku = koleksiBaru

    # metode publik
    def aksesInfoKoleksiBuku(self):
        return self.__infoKoleksiBuku()

class Buku(Perpustakaan):
    def __init__(self):
        # memanggil konstruktor kelas induk
        super().__init__()

    def demoBuku(self):
        # menggunakan getter dari kelas induk
        koleksiBuku = self.getKoleksiBuku()
        print(f"Koleksi buku dari kelas induk: {koleksiBuku}")

        # mengubah koleksi buku melalui setter kelas induk
        self.setKoleksiBuku("Koleksi buku baru dari kelas turunan")
        koleksiBukuBaru = self.getKoleksiBuku()
        print(f"Koleksi buku setelah diubah oleh turunan: {koleksiBukuBaru}")

        # mengakses metode privat dari kelas induk melalui metode publik
        hasilInfoKoleksi = self.aksesInfoKoleksiBuku()
        print(f"Hasil akses metode privat dari turunan: {hasilInfoKoleksi}")


# Membuat objek dari kelas turunan
objekBuku = Buku()
objekBuku.demoBuku()