class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f'Persegi Panjang dengan Panjang: {self.panjang} dan Lebar: {self.lebar}'

def main():
    try:
        # Membuat objek Persegi Panjang
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        
        persegi_panjang = PersegiPanjang(panjang, lebar)
        
        # Menampilkan informasi tentang objek
        print(persegi_panjang)
        
        # Menghitung dan menampilkan keliling
        keliling = persegi_panjang.hitung_keliling()
        print(f'Keliling: {keliling}')
        
        # Menghitung dan menampilkan luas
        luas = persegi_panjang.hitung_luas()
        print(f'Luas: {luas}')
    except ValueError:
        print("Input tidak valid. Mohon masukkan angka yang benar.")

if __name__ == "__main__":
    main()
    