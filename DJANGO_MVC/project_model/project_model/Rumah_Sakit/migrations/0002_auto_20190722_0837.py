# Generated by Django 2.2.3 on 2019-07-22 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rumah_Sakit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dokter',
            name='nama',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='obat',
            name='nama',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pasien',
            name='nama',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='resep',
            name='nama',
            field=models.CharField(max_length=255),
        ),
    ]
