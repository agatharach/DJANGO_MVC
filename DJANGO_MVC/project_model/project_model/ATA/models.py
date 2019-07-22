from django.db import models

# Create your models here.
class Direksi (models.Model):
    nama_lengkap = models.CharField(max_length=255)
    nomor_telepon = models.PositiveIntegerField()
    jabatan = models.TextField(max_length=17)

class Mentee (models.Model):
    nama_lengkap = models.CharField(max_length=255)
    nomor_telepon = models.PositiveIntegerField()
    nomor_absen = models.PositiveIntegerField()
    nilai_ratarata = models.DecimalField(decimal_places=2,max_digits=5) 	

class Mata_Pelajaran (models.Model):
    nama_pelajaran = models.CharField(max_length=50)
    jadwal_dimulai =  models.DateTimeField()
    jadwal_berakhir = models.DateTimeField()
    def __str__ (self):
        return self.nama_pelajaran

class Mentor (models.Model):
    nama_lengkap = models.CharField(max_length=255)
    nomor_telepon = models.PositiveIntegerField()
    mata_pelajaran = models.ForeignKey(Mata_Pelajaran, on_delete=models.CASCADE)

class Challenge (models.Model):
    nama_challenge = models.CharField(max_length=255)
    banyak_soal =  models.PositiveIntegerField()
    bobot_nilai = models.PositiveIntegerField()
    mata_pelajaran = models.ForeignKey(Mata_Pelajaran, on_delete=models.CASCADE)

class Live_Code (models.Model):
    nama_live_code = models.CharField(max_length=255)
    banyak_soal =  models.PositiveIntegerField()
    bobot_nilai = models.PositiveIntegerField()
    tanggal_pelaksanaan = models.DateTimeField()
    mata_pelajaran = models.ForeignKey(Mata_Pelajaran, on_delete=models.CASCADE)