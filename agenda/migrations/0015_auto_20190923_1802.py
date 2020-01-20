# Generated by Django 2.2.4 on 2019-09-23 22:02

import agenda.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0014_auto_20190923_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='hora_fin',
            field=models.TimeField(blank=True, default=datetime.datetime(2019, 9, 23, 18, 2, 21, 148269)),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='hora_inicio',
            field=models.TimeField(default=datetime.datetime(2019, 9, 23, 18, 2, 21, 148269)),
        ),
        migrations.CreateModel(
            name='Examenclinico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.TextField(blank=True)),
                ('fecha_archivo', models.DateField(default=datetime.datetime.now)),
                ('archivo', models.FileField(blank=True, upload_to=agenda.models.Examenclinico._generar_ruta_archivo)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.Agenda')),
            ],
        ),
    ]