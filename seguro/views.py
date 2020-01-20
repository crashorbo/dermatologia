from django.shortcuts import render
from django.views.generic import ListView, View, UpdateView, CreateView
from braces.views import JSONResponseMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render

from .models import Seguro, Segurocosto
from .forms import SeguroForm, SegurocostoForm
# Create your views here.

class TableAsJSON(JSONResponseMixin, View):
  model = Seguro

  def get(self, request, *args, **kwargs):
    col_name_map = {
      '0': 'nombre',
      '1': 'direccion',
      '2': 'telefono',
      '3': 'acciones',
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
  template_name = 'seguro/ajax/lista.html'
  model = Seguro
  context_object_name = 'servicios'

class AjaxCrearView(CreateView):
  model = Seguro
  form_class = SeguroForm
  template_name = 'seguro/ajax/crear.html'

  def form_valid(self, form):
    model = form.save(commit=False)
    model.save()
    return render(self.request, 'paciente/success.html')
        
class AjaxEditarView(UpdateView):
  template_name = 'seguro/ajax/editar.html'
  model = Seguro
  form_class = SeguroForm
  context_object_name = "seguro"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    print(self.kwargs['pk'])
    data = {'seguro': self.kwargs['pk']}
    segurocosto = SegurocostoForm(initial=data)
    context['segurocostoform'] = segurocosto
    return context

  def form_valid(self, form):
    model = form.save(commit=False)
    model.save()
    return render(self.request, 'paciente/success.html')

class AjaxEliminarView(View):
  def get(self, request):
    data = {
      'id': request.GET.get('id')
    }
    seguro = Seguro.objects.get(pk=request.GET.get('id'))
    seguro.delete()
    return JsonResponse(data)

class AjaxSegurocostoCrear(CreateView):
  model = Segurocosto
  form_class = SegurocostoForm
  template_name = 'seguro/ajax/crear.html'

  def form_valid(self, form):
    model = form.save(commit=False)
    serviciocosto = Segurocosto.objects.filter(seguro=model.seguro.id, servicio=model.servicio.id)
    if not serviciocosto:
      model.save()
    servicios = Segurocosto.objects.filter(seguro=model.seguro.id)
    return render(self.request, 'seguro/ajax/listaservicios.html', {'servicios': servicios})