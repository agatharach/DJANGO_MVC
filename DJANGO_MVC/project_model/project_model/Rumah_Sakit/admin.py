from django.contrib import admin
from .models import Dokter
from .models import Pasien
from .models import Resep
from .models import Obat

# Register your models here.
# admin.site.register(Dokter)
@admin.register(Dokter)
class Dokter(admin.ModelAdmin):
    list_display = ('id','nama', 'nomor_telepon','bidang','jadwal_praktek')
    ordering = ('id',)
    search_fields = ('nama', 'nomor_telepon')

# admin.site.register(Pasien)
@admin.register(Pasien)
class Pasien(admin.ModelAdmin):
    list_display = ('id','nama', 'nomor_telepon','alamat','keluhan')
    ordering = ('id',)
    search_fields = ('nama', 'nomor_telepon')

# admin.site.register(Resep)
@admin.register(Resep)
class Pasien(admin.ModelAdmin):
    list_display = ('id','nama', 'total_harga','kumpulan_obat')
    ordering = ('id',)
    search_fields = ('nama', 'total_harga')

# admin.site.register(Obat)
@admin.register(Obat)
class Obat(admin.ModelAdmin):
    list_display = ('id','nama', 'kandungan','khasiat')
    ordering = ('id',)
    search_fields = ('nama', 'kandungan')
