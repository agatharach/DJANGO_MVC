# Generated by Django 2.2.3 on 2019-07-22 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ATA', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='live_code',
            old_name='tanggal_pelaksaan',
            new_name='tanggal_pelaksanaan',
        ),
    ]
