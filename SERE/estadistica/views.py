from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.views import generic
from django.views.generic import View, TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
import json
from json import dumps
from django.db.models import Count

from catalogos.models import Categoria
from catalogos.models import SubCategoria
from catalogos.models import Producto,DETALLESACE,ProductoSINREGISTRO,ProductoINTERNO
from catalogos.forms import SubCategoriaForm,CategoriaForm,ProductoForm,ProductoFormSINREGISTRO,ProductoFormINTERNOS
from generales.views import SinPrivilegios
from catalogos.models import *
# Create your views here.
#Productos Externos
class Estadisticasdepartamentales(ListView):
    model = Producto
    template_name = "estadisticas_departamentos.html"
    context_object_name = "obj"
        #print('Listar productos')
    def get_queryset(self):
        p = Producto.objects.all()
        return p

    def get_context_data(self, **kwargs):
        print('Mandaremos algo')
        context = super().get_context_data(**kwargs)
        dep = Producto.objects.filter(subcategoria__categoria__pk=self.kwargs['pk']).values('subcategoria__categoria__pk').distinct()
        lista = Producto.objects.filter(subcategoria__categoria__pk=self.kwargs['pk']).order_by('-pk')
        #Productos Externos
        q1 = Producto.objects.filter(subcategoria__categoria__pk =self.kwargs['pk']).values(
                      'subcategoria__descripcion'
                   ).annotate(Count('pk'))
        q2 = ProductoINTERNO.objects.filter(subcategoria__categoria__pk =self.kwargs['pk']).values(
                      'subcategoria__descripcion'
                   ).annotate(Count('pk'))
        q2.union(q1)
        q3 = ProductoSINREGISTRO.objects.filter(subcategoria__categoria__pk =self.kwargs['pk']).values(
                      'subcategoria__descripcion'
                   ).annotate(Count('pk'))
        productos = q3.union(q2)
        print(productos)
        departamentos = []
        for p in Perfil.objects.filter(user = self.request.user):
            departamentos.append(
                    p.departamento.id
            )
        if  self.request.user.is_superuser:
            context['Departamentos'] = Categoria.objects.all()
        else:
            context['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
        return context
