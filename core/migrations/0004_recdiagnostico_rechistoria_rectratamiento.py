# Generated by Django 2.1.4 on 2019-07-19 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_recpaciente'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecDiagnostico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.TextField(blank=True, db_column='COD', null=True)),
                ('detalle', models.TextField(blank=True, db_column='DETALLE', null=True)),
            ],
            options={
                'db_table': 'rec_diagnostico',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RecHistoria',
            fields=[
                ('codigo', models.TextField(db_column='CODIGO', primary_key=True, serialize=False)),
                ('paciente', models.TextField(blank=True, db_column='PACIENTE', null=True)),
                ('procedenc', models.TextField(blank=True, db_column='PROCEDENC', null=True)),
                ('oculares', models.TextField(blank=True, db_column='OCULARES', null=True)),
                ('sitemicos', models.TextField(blank=True, db_column='SITEMICOS', null=True)),
                ('mot_consul', models.TextField(blank=True, db_column='MOT_CONSUL', null=True)),
                ('av_od1', models.TextField(blank=True, db_column='AV_OD1', null=True)),
                ('av_od2', models.TextField(blank=True, db_column='AV_OD2', null=True)),
                ('av_od3a', models.TextField(blank=True, db_column='AV_OD3A', null=True)),
                ('av_od3b', models.TextField(blank=True, db_column='AV_OD3B', null=True)),
                ('av_od3c', models.TextField(blank=True, db_column='AV_OD3C', null=True)),
                ('av_od4', models.TextField(blank=True, db_column='AV_OD4', null=True)),
                ('av_od5', models.TextField(blank=True, db_column='AV_OD5', null=True)),
                ('av_od6', models.TextField(blank=True, db_column='AV_OD6', null=True)),
                ('av_od7', models.TextField(blank=True, db_column='AV_OD7', null=True)),
                ('av_od8', models.TextField(blank=True, db_column='AV_OD8', null=True)),
                ('av_od9', models.TextField(blank=True, db_column='AV_OD9', null=True)),
                ('av_od10a', models.TextField(blank=True, db_column='AV_OD10A', null=True)),
                ('av_od10b', models.TextField(blank=True, db_column='AV_OD10B', null=True)),
                ('av_od10c', models.TextField(blank=True, db_column='AV_OD10C', null=True)),
                ('av_oi1', models.TextField(blank=True, db_column='AV_OI1', null=True)),
                ('av_oi2', models.TextField(blank=True, db_column='AV_OI2', null=True)),
                ('av_oi3a', models.TextField(blank=True, db_column='AV_OI3A', null=True)),
                ('av_oi3b', models.TextField(blank=True, db_column='AV_OI3B', null=True)),
                ('av_oi3c', models.TextField(blank=True, db_column='AV_OI3C', null=True)),
                ('av_oi4', models.TextField(blank=True, db_column='AV_OI4', null=True)),
                ('av_oi5', models.TextField(blank=True, db_column='AV_OI5', null=True)),
                ('av_oi6', models.TextField(blank=True, db_column='AV_OI6', null=True)),
                ('av_oi7', models.TextField(blank=True, db_column='AV_OI7', null=True)),
                ('av_oi8', models.TextField(blank=True, db_column='AV_OI8', null=True)),
                ('av_oi9', models.TextField(blank=True, db_column='AV_OI9', null=True)),
                ('av_oi10a', models.TextField(blank=True, db_column='AV_OI10A', null=True)),
                ('av_oi10b', models.TextField(blank=True, db_column='AV_OI10B', null=True)),
                ('av_oi10c', models.TextField(blank=True, db_column='AV_OI10C', null=True)),
                ('adicion', models.TextField(blank=True, db_column='ADICION', null=True)),
                ('to_od', models.TextField(blank=True, db_column='TO_OD', null=True)),
                ('to_oi', models.TextField(blank=True, db_column='TO_OI', null=True)),
                ('biom_od', models.TextField(blank=True, db_column='BIOM_OD', null=True)),
                ('biom_oi', models.TextField(blank=True, db_column='BIOM_OI', null=True)),
                ('fondo_od', models.TextField(blank=True, db_column='FONDO_OD', null=True)),
                ('fondo_oi', models.TextField(blank=True, db_column='FONDO_OI', null=True)),
                ('otros', models.TextField(blank=True, db_column='OTROS', null=True)),
                ('fecha', models.DateField(blank=True, db_column='FECHA', null=True)),
                ('monto', models.FloatField(blank=True, db_column='MONTO', null=True)),
                ('eod', models.TextField(blank=True, db_column='EOD', null=True)),
                ('ciod', models.TextField(blank=True, db_column='CIOD', null=True)),
                ('ejeod', models.TextField(blank=True, db_column='EJEOD', null=True)),
                ('eoi', models.TextField(blank=True, db_column='EOI', null=True)),
                ('cioi', models.TextField(blank=True, db_column='CIOI', null=True)),
                ('ejeoi', models.TextField(blank=True, db_column='EJEOI', null=True)),
                ('dp1', models.TextField(blank=True, db_column='DP1', null=True)),
                ('adicion1', models.TextField(blank=True, db_column='ADICION1', null=True)),
                ('dp2', models.TextField(blank=True, db_column='DP2', null=True)),
                ('otros1', models.TextField(blank=True, db_column='OTROS1', null=True)),
                ('rec1', models.TextField(blank=True, db_column='REC1', null=True)),
                ('rec2', models.TextField(blank=True, db_column='REC2', null=True)),
                ('rec3', models.TextField(blank=True, db_column='REC3', null=True)),
                ('rec4', models.TextField(blank=True, db_column='REC4', null=True)),
                ('rec5', models.TextField(blank=True, db_column='REC5', null=True)),
                ('rec6', models.TextField(blank=True, db_column='REC6', null=True)),
                ('rec7', models.TextField(blank=True, db_column='REC7', null=True)),
                ('rec8', models.TextField(blank=True, db_column='REC8', null=True)),
                ('rec9', models.TextField(blank=True, db_column='REC9', null=True)),
                ('rec10', models.TextField(blank=True, db_column='REC10', null=True)),
                ('recet', models.TextField(blank=True, db_column='RECET', null=True)),
            ],
            options={
                'db_table': 'rec_historia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RecTratamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.TextField(blank=True, db_column='COD', null=True)),
                ('detalle', models.TextField(blank=True, db_column='DETALLE', null=True)),
            ],
            options={
                'db_table': 'rec_tratamiento',
                'managed': False,
            },
        ),
    ]
