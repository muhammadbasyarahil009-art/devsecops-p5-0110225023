
import unittest
import tempfile
from pathlib import Path

from mahasiswa import (
    tambah_mahasiswa,
    daftar_mahasiswa,
    cari_mahasiswa,
    hapus_mahasiswa
)


class TestMahasiswa(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_data = Path(self.temp_dir.name) / "data.json"

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_tambah_mahasiswa(self):
        tambah_mahasiswa("12345", "Budi", self.file_data)
        self.assertEqual(len(daftar_mahasiswa(self.file_data)), 1)

    def test_nim_duplikat(self):
        tambah_mahasiswa("12345", "Budi", self.file_data)

        with self.assertRaises(ValueError):
            tambah_mahasiswa("12345", "Andi", self.file_data)

    def test_cari_mahasiswa(self):
        tambah_mahasiswa("12345", "Budi", self.file_data)
        hasil = cari_mahasiswa("12345", self.file_data)
        self.assertEqual(hasil["nama"], "Budi")

    def test_hapus_mahasiswa(self):
        tambah_mahasiswa("12345", "Budi", self.file_data)
        self.assertTrue(hapus_mahasiswa("12345", self.file_data))
        self.assertEqual(daftar_mahasiswa(self.file_data), [])

    def test_nim_harus_angka(self):
        with self.assertRaises(ValueError):
            tambah_mahasiswa("ABC", "Budi", self.file_data)


if __name__ == "__main__":
    unittest.main()
