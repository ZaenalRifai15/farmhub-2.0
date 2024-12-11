from django.db import models

# Create your models here.
class Pengguna(models.Model):
    nama = models.CharField(max_length=250)
    no_telpon = models.CharField(max_length=12)
    password = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    lokasi = models.TextField

    def __str__(self):
        return f"{self.email} ({self.password})"
