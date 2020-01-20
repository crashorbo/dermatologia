from django import forms
from .models import Paciente, Archivopdf

class PacienteForm(forms.ModelForm):
  class Meta:
    model = Paciente
    fields = ('nombres', 'apellidos', 'progenitor', 'email', 'fecha_nacimiento', 'documento', 'nro_documento', 'direccion', 'telefono', 'ocupacion')

    widgets = {
      'nombres': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
      'apellidos': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
      'progenitor': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
      'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm'}),
      'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control form-control-sm fecha'}),
      'documento': forms.Select(attrs={'class': 'form-control form-control-sm'}),
      'nro_documento': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
      'ocupacion': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
      'telefono': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
      'direccion': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 2}),
    }

class ArchivopdfForm(forms.ModelForm):
  class Meta:
    model = Archivopdf
    fields = ('paciente', 'fecha_documento', 'archivo', 'nombre', 'descripcion')

    widgets = {
      'fecha_documento': forms.DateInput(attrs={'class': 'form-control fecha'}),
      'nombre': forms.TextInput(attrs={'class': 'form-control'}),
      'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
      'archivo': forms.FileInput(attrs={'class': 'dropify'}),
    }