from django.contrib import admin
from .models import Merek, Motor, Peminjaman

@admin.register(Merek)
class MerekAdmin(admin.ModelAdmin):
    list_display = ('nama_merek', 'deskripsi')

@admin.register(Motor)
class MotorAdmin(admin.ModelAdmin):
    list_display = ('nama', 'merek', 'stok', 'harga_per_hari')
    list_filter = ('merek',)
    search_fields = ('nama', 'merek__nama_merek')

@admin.register(Peminjaman)
class PeminjamanAdmin(admin.ModelAdmin):
    list_display = ('nama_peminjam', 'motor', 'tanggal_pinjam', 'status')
    list_filter = ('status',)
    search_fields = ('nama_peminjam', 'nik')
