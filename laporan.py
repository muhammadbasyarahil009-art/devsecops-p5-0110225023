
def buat_laporan(data):
    return {
        "total_mahasiswa": len(data),
        "daftar_nama": [m["nama"] for m in data]
    }
