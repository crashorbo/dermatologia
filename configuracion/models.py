from django.db import models
from django.urls import reverse
from django.db.models import Q
from django.db.models.query import QuerySet

class MyModelMixin(object):

  def q_for_search_word(self, word):
    return Q(nombre__icontains=word) | Q(direccion__icontains=word) | Q(telefono__icontains=word)

  def q_for_search(self, search):
    q = Q()
    if search:
        searches = search.split()
        for word in searches:
            q = q & self.q_for_search_word(word)
    return q

  def filter_on_search(self, search):
    return self.filter(self.q_for_search(search))

class MyModelQuerySet(QuerySet, MyModelMixin):
  pass

class MyModelManager(models.Manager, MyModelMixin):
  
  def get_queryset(self):
    return MyModelQuerySet(self.model, using=self._db)

# Create your models here.
class Tipolente(models.Model):
  nombre = models.CharField(max_length=200)
  descripcion = models.TextField(blank=True)

  objects = MyModelManager()

  def __str__(self):
    return self.nombre

  def as_list(self):
    return [self.nombre,
      self.descripcion,
      '<button class="tipolente-editar btn btn-xs btn-warning m-l-5" data-url='+reverse('tipolente-ajax-editar', args=[self.id])+'><i class="fa fa-edit"></i></button><button class="tipolente-eliminar btn btn-xs btn-danger m-l-5" data-url='+reverse('tipolente-ajax-eliminar')+' data-id='+str(self.id)+'><i class="fa fa-close"></i></button>']

  class Meta:
    ordering = ('nombre',)
