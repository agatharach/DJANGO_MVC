from django.db import models

# Create your models here.
class Hewan (models.Model):
    nama = models.CharField(max_length=255)
    species =  models.CharField(max_length=17)
    berat = models.CharField(max_length=17)
    umur = models.PositiveIntegerField()

class Kandang (models.Model):
    nama = models.CharField(max_length=255)
    isi_kandang =  models.CharField(max_length=255)
    luas_kandang = models.PositiveIntegerField()
    

class Penjaga (models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon =  models.PositiveIntegerField()
    jadwal_jaga = models.DateTimeField()

class Pengunjung (models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon =  models.PositiveIntegerField()
    hari_berkunjung = models.DateTimeField()