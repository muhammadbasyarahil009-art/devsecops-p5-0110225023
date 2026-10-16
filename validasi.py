
def validasi_nim(nim):
    nim = nim.strip()

    if not nim:
        raise ValueError("NIM tidak boleh kosong.")

    if not nim.isdigit():
        raise ValueError("NIM harus berupa angka.")

    return nim


def validasi_nama(nama):
    nama = nama.strip()

    if len(nama) < 2:
        raise ValueError("Nama minimal 2 karakter.")

    return nama
