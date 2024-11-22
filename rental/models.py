from django.db import models
from django.utils.timezone import now

class Merek(models.Model):
    nama_merek = models.CharField(max_length=150)
    deskripsi = models.TextField(max_length=250)
    
    def __str__(self):
        return self.nama_merek
    
class Motor(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    merek = models.ForeignKey(Merek, on_delete=models.CASCADE, related_name='motors')
    stok = models.PositiveIntegerField(default=0)
    harga_per_hari = models.DecimalField(max_digits=10, decimal_places=2)
    gambar = models.ImageField(upload_to='motor_images/')

    def __str__(self):
        return self.nama


class Peminjaman(models.Model):
    STATUS_CHOICES = [
        ('DIPESAN', 'Dipesan'),
        ('DIPINJAM', 'Dipinjam'),
        ('DIKEMBALIKAN', 'Dikembalikan'),
    ]

    nik = models.CharField(max_length=16)
    nama_peminjam = models.CharField(max_length=100)
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE, related_name='peminjamans')
    tanggal_pinjam = models.DateField(default=now)
    tanggal_kembali = models.DateField()
    jumlah_bayar = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sudah_bayar = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='DIPESAN'
    )
    no_polisi = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nama_peminjam} - {self.motor.nama}"
# Create your models here.
