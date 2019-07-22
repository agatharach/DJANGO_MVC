from django.contrib import admin
from .models import Hewan
from .models import Kandang
from .models import Penjaga
from .models import Pengunjung

# Register your models here.
# admin.site.register(Hewan)
@admin.register(Hewan)
class Hewan(admin.ModelAdmin):
    list_display = ('id','nama', 'species', 'berat','umur')
    ordering = ('id',)
    search_fields = ('nama', 'species')
# admin.site.register(Kandang)
@admin.register(Kandang)
class Kandang(admin.ModelAdmin):
    list_display = ('id','nama', 'isi_kandang', 'luas_kandang')
    ordering = ('id',)
    search_fields = ('nama', 'isi_kandang')

# admin.site.register(Penjaga)
@admin.register(Penjaga)
class Penjaga(admin.ModelAdmin):
    list_display = ('id','nama', 'nomor_telepon', 'jadwal_jaga')
    ordering = ('id',)
    search_fields = ('nama', 'nomor_telepon')

# admin.site.register(Pengunjung)
@admin.register(Pengunjung)
class Pengunjung(admin.ModelAdmin):
    list_display = ('id','nama', 'nomor_telepon','hari_berkunjung')
    ordering = ('id',)
    search_fields = ('nama', 'nomor_telepon')