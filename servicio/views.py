from django.shortcuts import render
from django.views.generic import ListView, View, UpdateView, CreateView
from braces.views import JSONResponseMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render

from .models import Servicio
from .forms import ServicioForm
# Create your views here.

class TableAsJSON(JSONResponseMixin, View):
  model = Servicio

  def get(self, request, *args, **kwargs):
    col_name_map = {
      '0': 'nombre',
      '1': 'costo',
      '2': 'acciones',
    }
    object_list = self.model.objects.all()
    search_text = request.GET.get('sSearch', '').lower()
    start = int(request.GET.get('iDisplayStart', 0))
    delta = int(request.GET.get('iDisplayLength', 50))
    sort_dir = request.GET.get('sSortDir_0', 'asc')
    sort_col = int(request.GET.get('iSortCol_0', 0))
    sort_col_name = request.GET.get('mDataProp_%s' % sort_col, '1')
    sort_dir_prefix = (sort_dir == 'desc' and '-' or '')

    if sort_col_name in col_name_map:
      sort_col = col_name_map[sort_col_name]
      object_list = object_list.order_by('%s%s' % (sort_dir_prefix, sort_col))

    filtered_object_list = object_list
    if len(search_text) > 0:
      filtered_object_list = object_list.filter_on_search(search_text)

    json = {
      "iTotalRecords": object_list.count(),
      "iTotalDisplayRecords": filtered_object_list.count(),
      "sEcho": request.GET.get('sEcho', 1),
      "aaData": [obj.as_list() for obj in filtered_object_list[start:(start+delta)]]
    }
    return self.render_json_response(json)

class AjaxListView(ListView):
  template_name = 'servicio/ajax/lista.html'
  model = Servicio
  context_object_name = 'servicios'

class AjaxCrearView(CreateView):
  model = Servicio
  form_class = ServicioForm
  template_name = 'servicio/ajax/crear.html'

  def form_valid(self, form):
    model = form.save(commit=False)
    model.save()
    return render(self.request, 'paciente/success.html')
        
  
class AjaxEditarView(UpdateView):
  template_name = 'servicio/ajax/editar.html'
  model = Servicio
  form_class = ServicioForm
  context_object_name = "servicio"

  def form_valid(self, form):
    model = form.save(commit=False)
    model.save()
    return render(self.request, 'paciente/success.html')

class AjaxEliminarView(View):
  def get(self, request):
    data = {
      'id': request.GET.get('id')
    }
    servicio = Servicio.objects.get(pk=request.GET.get('id'))
    servicio.delete()
    return JsonResponse(data)