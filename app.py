
from mahasiswa import (
    tambah_mahasiswa,
    daftar_mahasiswa,
    cari_mahasiswa,
    hapus_mahasiswa
)
from laporan import buat_laporan


def main():
    while True:
        print("\n=== MANAJEMEN DATA MAHASISWA ===")
        print("1. Tambah mahasiswa")
        print("2. Tampilkan mahasiswa")
        print("3. Cari mahasiswa")
        print("4. Hapus mahasiswa")
        print("5. Laporan")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        try:
            if pilihan == "1":
                nim = input("NIM: ")
                nama = input("Nama: ")
                tambah_mahasiswa(nim, nama)
                print("Mahasiswa berhasil ditambahkan.")

            elif pilihan == "2":
                data = daftar_mahasiswa()
                for m in data:
                    print(f'{m["nim"]} - {m["nama"]}')

                if not data:
                    print("Belum ada data mahasiswa.")

            elif pilihan == "3":
                nim = input("Masukkan NIM: ")
                hasil = cari_mahasiswa(nim)
                print(hasil if hasil else "Mahasiswa tidak ditemukan.")

            elif pilihan == "4":
                nim = input("NIM yang dihapus: ")
                berhasil = hapus_mahasiswa(nim)
                print("Data berhasil dihapus." if berhasil
                      else "Mahasiswa tidak ditemukan.")

            elif pilihan == "5":
                laporan = buat_laporan(daftar_mahasiswa())
                print("Total mahasiswa:", laporan["total_mahasiswa"])
                print("Nama mahasiswa:", laporan["daftar_nama"])

            elif pilihan == "0":
                print("Aplikasi selesai.")
                break

            else:
                print("Pilihan tidak valid.")

        except (ValueError, OSError) as error:
            print("Terjadi kesalahan:", error)


if __name__ == "__main__":
    main()
