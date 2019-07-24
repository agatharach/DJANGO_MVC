from django.contrib import admin
from .models import Direksi
from .models import Mentee
from .models import Mentor
from .models import Mata_Pelajaran
from .models import Challenge
from .models import Live_Code

# Register your models here.
# admin.site.register(Direksi)
@admin.register(Direksi)
class Direksi(admin.ModelAdmin):
    list_display = ('id','nama_lengkap', 'nomor_telepon', 'jabatan')
    ordering = ('id',)
    search_fields = ('nama_lengkap', 'jabatan')

# admin.site.register(Challenge)

@admin.register(Challenge)
class Challenge(admin.ModelAdmin):
    list_display = ('id','nama_challenge', 'banyak_soal', 'bobot_nilai','mata_pelajaran')
    ordering = ('id',)
    search_fields = ('nama_challenge', 'banyak_soal')
    

# admin.site.register(Mentee)
@admin.register(Mentee)
class Mentee(admin.ModelAdmin):
    list_display = ('id','nama_lengkap', 'nomor_telepon', 'nomor_absen','nilai_ratarata')
    ordering = ('id',)
    search_fields = ('nama_lengkap', 'nomor_telepon')

# admin.site.register(Mata_Pelajaran)
@admin.register(Mata_Pelajaran)
class Mata_Pelajaran(admin.ModelAdmin):
    list_display = ('id','nama_pelajaran', 'jadwal_dimulai', 'jadwal_berakhir')
    ordering = ('id',)
    search_fields = ('nama_pelajaran', 'jadwal_dimulai')

# admin.site.register(Mentor)
@admin.register(Mentor)
class Mentor(admin.ModelAdmin):
    list_display = ('id','nama_lengkap', 'nomor_telepon', 'mata_pelajaran')
    ordering = ('id',)
    search_fields = ('nama_lengkap', 'nomor_telepon')

# admin.site.register(Live_Code)
@admin.register(Live_Code)
class Live_Code(admin.ModelAdmin):
    list_display = ('id','nama_live_code', 'banyak_soal', 'bobot_nilai','tanggal_pelaksanaan','mata_pelajaran')
    ordering = ('id',)
    search_fields = ('nama_live_code', 'banyak_soal')