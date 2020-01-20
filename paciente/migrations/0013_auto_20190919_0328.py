# Generated by Django 2.2.4 on 2019-09-19 07:28

import datetime
from django.db import migrations, models
import paciente.models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0012_auto_20190917_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='codigo',
        ),
        migrations.AddField(
            model_name='paciente',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='paciente',
            name='progenitor',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='archivopdf',
            name='archivo',
            field=models.FileField(blank=True, upload_to=paciente.models.Archivopdf._generar_ruta_archivo),
        ),
        migrations.AlterField(
            model_name='archivopdf',
            name='fecha',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
