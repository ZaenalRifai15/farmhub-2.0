from django.db import models

# Create your models here.
class Pengguna(models.Model):
    nama = models.CharField(max_length=250)
    no_telpon = models.CharField(max_length=12)
    password = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    lokasi = models.TextField()

    def __str__(self):
        return f"{self.email} ({self.password})"
    
class Produk(models.Moodel):
    nama_produk = models.CharField(max_length=250)
    harga = models.PositiveIntegerField()
    deskripsi_produk = models.TextField()

    def __str__(self):
        return f"{self.nama_produk} ({self.harga})"
    
class Fotovideo(models.Model):
    nama_file = models.CharField(max_length=250)

    def __str__(self):
        return self.nama_file
    
class Stok(models.Model):
    jumlah = models.PositiveIntegerField()
    tanggal_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.jumlah
    
class Jenisproduk(models.Model):
    nama_jenis = models.CharField(max_length=250)

    def __str__(self):
        return self.nama_jenis
    
class Review(models.Model):
    rating = models.PositiveIntegerField()
    komentar = models.TextField()

    def __str__(self):
        return f"{self.rating} ({self.komentar})"
    
class Transaksi(models.Model):
    tanggal_transaksi = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tanggal_transaksi} ({self.status})"