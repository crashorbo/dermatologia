from django import forms
from django.forms.models import inlineformset_factory
from .models import Agenda, Diagnostico, Tratamiento, Agendaserv, Receta, Reconsulta, Examenclinico
from dal import autocomplete
from paciente.models import Paciente
from seguro.models import Seguro
from servicio.models import Servicio
from medicamento.models import Medicamento

class AgendaForm(forms.ModelForm):
  paciente = forms.ModelChoiceField(queryset=Paciente.objects.all(), empty_label="Seleccionar Paciente", widget=autocomplete.ModelSelect2(url='paciente-autocomplete', attrs={'class': 'form-control form-control-sm'}))
  seguro = forms.ModelChoiceField(queryset=Seguro.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
  
  class Meta:
    model = Agenda
    fields = ('paciente', 'seguro', 'fecha', 'fecha_consulta', 'hora_inicio', 'hora_fin', 'tipo', 'prioridad', 'procedencia',
              'matricula', 'tipo_beneficiario', 'antecedentes', 'motivo_consulta', 'control')

    widgets = {
      'fecha': forms.DateInput(attrs={'class': 'form-control fecha form-control-sm'}),
      'hora_inicio': forms.TimeInput(format='%H:%M', attrs={'class': 'form-control form-control-sm clockpicker','data-placement':'bottom', 'data-align':'top', 'data-autoclose':'true'}),
      'hora_fin': forms.TimeInput(format='%H:%M', attrs={'class': 'form-control form-control-sm clockpicker','data-placement':'bottom', 'data-align':'top', 'data-autoclose':'true'}),
      'tipo': forms.Select(attrs={'class': 'form-control form-control-sm'}),
      'prioridad': forms.Select(attrs={'class': 'form-control form-control-sm'}),
      'procedencia': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
      'matricula': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
      'tipo_beneficiario': forms.Select(attrs={'class': 'form-control form-control-sm'}),
      'antecedentes': forms.Textarea(attrs={'class': 'form-control form-control-sm autoguardado', 'tabindex': 1, 'rows': 2}),
      'motivo_consulta': forms.Textarea(attrs={'class': 'form-control form-control-sm autoguardado', 'tabindex': 3, 'rows': 2}),      
    }

class DiagnosticoForm(forms.ModelForm):
  class Meta:
    model = Diagnostico
    fields = ('detalle', 'agenda')
    widgets = {
      'agenda': forms.HiddenInput(),
      'detalle': forms.TextInput(attrs={'class': 'form-control form-control-sm enviod', 'tabindex': 41}),
    }

class TratamientoForm(forms.ModelForm):
  class Meta:
    model = Tratamiento
    fields = ('detalle', 'agenda', 'cantidad')
    widgets = {
      'agenda': forms.HiddenInput(),
      'cantidad': forms.NumberInput(attrs={'class': 'form-control form-control-sm envioct'}),
      'detalle': forms.TextInput(attrs={'class': 'form-control form-control-sm enviot', 'tabindex': 42}),
    }

class AgendaservicioForm(forms.ModelForm):
  servicio = forms.ModelChoiceField(queryset=Servicio.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control form-control-sm costoserv'}))
  class Meta:
    model = Agendaserv
    fields = ('agenda','servicio', 'costo', 'descuento')
    widgets = {
      'agenda': forms.HiddenInput(),
      'costo': forms.NumberInput(attrs={'class': 'form-control form-control-sm addcosto', 'readonly': True}),
      'descuento': forms.CheckboxInput(attrs={'class': 'form-control form-control-sm'}),
    }

class AgendaservForm(forms.ModelForm):
  servicio = forms.ModelChoiceField(queryset=Servicio.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control form-control-sm costoserv'}))
  class Meta:
    model = Agendaserv
    fields = ('servicio', 'costo', 'estado', 'descuento')
    widgets = {
      'costo': forms.NumberInput(attrs={'class': 'form-control form-control-sm addcosto', 'readonly': True}),
      'estado': forms.CheckboxInput(attrs={'class': 'filled-in chk-col-red form-control-sm'}),
      'descuento': forms.CheckboxInput(attrs={'class': 'filled-in chk-col-blue form-control-sm'}),
    }

ServicioFormset = inlineformset_factory(Agenda, Agendaserv, AgendaservForm, can_delete=False, extra=1)

class RecetaForm(forms.ModelForm):
  medicamento = forms.ModelChoiceField(queryset=Medicamento.objects.all(), empty_label="Seleccionar Medicamento", widget=autocomplete.ModelSelect2(url='medicamento-autocomplete', attrs={'class': 'form-control form-control-sm'}))
  class Meta:
    model = Receta
    fields = ('medicamento','agenda', 'cantidad', 'indicacion','presentacion')
    widgets = {
      'agenda': forms.HiddenInput(),
      'cantidad': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
      'presentacion': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
      'indicacion': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 2}),
    }

class ReconsultaForm(forms.ModelForm):
  class Meta:
    model = Reconsulta
    fields = ('detalle', 'agenda')
    widgets = {
      'agenda': forms.HiddenInput(),
      'detalle': forms.Textarea(attrs={'class': 'form-control form-control-sm enviocontrol', 'rows': 2, 'tabindex': 43}),
    }

class ExamenclinicoForm(forms.ModelForm):
  class Meta:
    model = Examenclinico
    fields = ('agenda', 'detalle', 'fecha_archivo', 'archivo')
    widgets = {
      'agenda': forms.HiddenInput(),
      'detalle': forms.Textarea(attrs={'class': 'form-control form-control-sm enviocontrol', 'rows': 2, 'tabindex': 43}),
      'fecha_archivo': forms.DateInput(attrs={'class': 'form-control fecha form-control-sm'}),
      'archivo': forms.FileInput(attrs={'class': "dropify", 'capture': 'camera', 'data-height': '120', 'data-default-file': '/media/Imagenes/no-image.png'})
    }