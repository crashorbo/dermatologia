# Generated by Django 2.2.4 on 2019-09-17 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0007_auto_20190820_1945'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diagnostico',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='tratamiento',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='agenda',
            name='hora_fin',
            field=models.TimeField(blank=True, default=datetime.datetime(2019, 9, 17, 15, 32, 46, 644069)),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='hora_inicio',
            field=models.TimeField(default=datetime.datetime(2019, 9, 17, 15, 32, 46, 644069)),
        ),
    ]