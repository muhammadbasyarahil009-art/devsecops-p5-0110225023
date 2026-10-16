
from validasi import validasi_nim, validasi_nama
from penyimpanan import baca_data, simpan_data, FILE_DATA


def tambah_mahasiswa(nim, nama, file_path=FILE_DATA):
    nim = validasi_nim(nim)
    nama = validasi_nama(nama)
    data = baca_data(file_path)

    if any(m["nim"] == nim for m in data):
        raise ValueError("NIM sudah terdaftar.")

    data.append({"nim": nim, "nama": nama})
    simpan_data(data, file_path)


def daftar_mahasiswa(file_path=FILE_DATA):
    return baca_data(file_path)


def cari_mahasiswa(nim, file_path=FILE_DATA):
    nim = validasi_nim(nim)
    data = baca_data(file_path)

    for mahasiswa in data:
        if mahasiswa["nim"] == nim:
            return mahasiswa

    return None


def hapus_mahasiswa(nim, file_path=FILE_DATA):
    nim = validasi_nim(nim)
    data = baca_data(file_path)
    data_baru = [m for m in data if m["nim"] != nim]

    if len(data_baru) == len(data):
        return False

    simpan_data(data_baru, file_path)
    return True
