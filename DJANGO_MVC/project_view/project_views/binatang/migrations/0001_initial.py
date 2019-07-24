# Generated by Django 2.2.3 on 2019-07-23 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NamaHewan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_hewan', models.CharField(max_length=255)),
                ('species', models.CharField(max_length=17)),
                ('berat', models.CharField(max_length=17)),
                ('umur', models.PositiveIntegerField()),
            ],
        ),
    ]
