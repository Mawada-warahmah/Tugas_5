# Parent Class - Kendaraan
class Kendaraan:
    def __init__(self, merk, kecepatan, konsumsi_bahan_bakar):
        self.merk = merk
        self.kecepatan = kecepatan
        self.konsumsi_bahan_bakar = konsumsi_bahan_bakar  # liter per km

    def info_kendaraan(self):
        return f"Merk: {self.merk}, Kecepatan: {self.kecepatan} km/jam, Konsumsi Bahan Bakar: {self.konsumsi_bahan_bakar} L/km"

    def hitung_biaya_bahan_bakar(self, jarak, harga_per_liter):
        total_liter = jarak * self.konsumsi_bahan_bakar
        total_biaya = total_liter * harga_per_liter
        return f"Biaya bahan bakar untuk {jarak} km: Rp {total_biaya:.2f}"

# Child Class - Mobil
class Mobil(Kendaraan):
    def __init__(self, merk, kecepatan, konsumsi_bahan_bakar, jumlah_pintu):
        super().__init__(merk, kecepatan, konsumsi_bahan_bakar)
        self.jumlah_pintu = jumlah_pintu

    def info_kendaraan(self):
        return f"{super().info_kendaraan()}, Jumlah Pintu: {self.jumlah_pintu}"

# Child Class - Motor
class Motor(Kendaraan):
    def __init__(self, merk, kecepatan, konsumsi_bahan_bakar, jenis):
        super().__init__(merk, kecepatan, konsumsi_bahan_bakar)
        self.jenis = jenis  # Jenis motor, misalnya 'sport' atau 'moped'

    def info_kendaraan(self):
        return f"{super().info_kendaraan()}, Jenis Motor: {self.jenis}"

# Contoh Penggunaan
mobil1 = Mobil("Toyota Avanza", 120, 0.1, 4)
motor1 = Motor("Yamaha R15", 80, 0.05, "sport")

# Menampilkan informasi kendaraan
print(mobil1.info_kendaraan())
print(motor1.info_kendaraan())

# Menghitung biaya bahan bakar
jarak = 100  # dalam km
harga_per_liter = 15000  # dalam rupiah

print(mobil1.hitung_biaya_bahan_bakar(jarak, harga_per_liter))
print(motor1.hitung_biaya_bahan_bakar(jarak, harga_per_liter))