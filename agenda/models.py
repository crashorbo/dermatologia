from django.db import models
from django.utils import timezone
from uuid import uuid4
import os
from datetime import datetime, timedelta, date
from paciente.models import Paciente
from seguro.models import Seguro
from servicio.models import Servicio
from configuracion.models import Tipolente
from medicamento.models import Medicamento


class Agenda(models.Model):
    TIPO_CHOICE = (
        (0, 'PARTICULAR'),
        (1, 'SEGURO'),
    )

    PRIORIDAD_CHOICE = (
        ('LEVE', 'LEVE'),
        ('MODERADO', 'MODERADO'),
        ('URGENTE', 'URGENTE'),
    )

    BENEFICIARIO_CHOICE = (
        ('ACTIVO', 'ACTIVO'),
        ('BENFICIARIO', 'BENFICIARIO'),
        ('RENTISTA', 'RENTISTA'),
    )

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    seguro = models.ForeignKey(Seguro, on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.now)
    fecha_consulta = models.DateField(default=datetime.now)
    hora_inicio = models.TimeField(default=datetime.now())
    hora_fin = models.TimeField(default=datetime.now(), blank=True)
    estado = models.IntegerField(default=0)
    deleted = models.BooleanField(default=False)
    prioridad = models.CharField(
        max_length=20, choices=PRIORIDAD_CHOICE, default='LEVE')
    tipo = models.IntegerField(choices=TIPO_CHOICE, default=0)
    procedencia = models.CharField(max_length=100, blank=True)
    matricula = models.CharField(max_length=100, blank=True)
    tipo_beneficiario = models.CharField(
        max_length=20, choices=BENEFICIARIO_CHOICE, default='ACTIVO')
    antecedentes = models.TextField(blank=True)
    motivo_consulta = models.TextField(blank=True)
    control = models.BooleanField(default=False)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ('fecha',)


class Diagnostico(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    detalle = models.CharField(max_length=200)

    class Meta:
        ordering = ['id']


class Tratamiento(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    detalle = models.CharField(max_length=200)

    class Meta:
        ordering = ['id']


class Agendaserv(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    costo = models.DecimalField(max_digits=5, decimal_places=2)
    fecha = models.DateField(default=timezone.now)
    hora = models.DateTimeField(default=timezone.now)
    estado = models.BooleanField(default=True)
    descuento = models.BooleanField(default=False)


class Receta(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    presentacion = models.CharField(blank=True, max_length=100)
    cantidad = models.IntegerField(default=1)
    indicacion = models.TextField(blank=True)


class Reconsulta(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    detalle = models.TextField()


class Examenclinico(models.Model):
    def _generar_ruta_archivo(self, instance, filename):
        # El primer paso es extraer la extension de la imagen del
        # archivo original
        extension = os.path.splitext(filename)[1][1:]

        # Generamos la ruta relativa a MEDIA_ROOT donde almacenar
        # el archivo, usando la fecha actual (año/mes)
        ruta = os.path.join('Imagenes', date.today().strftime("%Y/%m"))

        # Generamos el nombre del archivo con un identificador
        # aleatorio, y la extension del archivo original.
        nombre_archivo = '{}.{}'.format(uuid4().hex, extension)

        # Devolvermos la ruta completa
        return os.path.join(ruta, nombre_archivo)

    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    detalle = models.TextField(blank=True)
    fecha_archivo = models.DateField(default=datetime.now)
    archivo = models.FileField(upload_to=_generar_ruta_archivo, blank=True)
    fecha = models.DateTimeField(auto_now=True)
