from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.db.models import F, Q, When
from json import dumps
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from catalogos.models import Categoria,Perfil,Producto,ProductoINTERNO,ProductoSINREGISTRO
from django.views import generic

from django.db.models.functions import Extract
# Create your views here.
class SinPrivilegios(PermissionRequiredMixin):
    login_url='generales:sin_privilegios'
    raise_exception=False
    redirect_field_name="redirecto_to"
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy(self.login_url))

class HomePage(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Pagina de Inicio')


class Home(generic.TemplateView):
    template_name='generales/home.html'

class Home_user(LoginRequiredMixin, generic.TemplateView):
    template_name='generales/home_user.html'
    login_url='generales:login'
    def get_context_data(self, **kwargs):
        #Declaramos el arreglo departamento
        dep_grap = []
        departamentos = []
        context = super(Home_user, self).get_context_data(**kwargs)
        #recorremos los departamentos a los cuales tiene acceso el usuario

        for p in Perfil.objects.filter(user = self.request.user):
            departamentos.append(
                    p.departamento.id
            )
            dep_grap.append(
                    p.departamento.descripcion
            )	
        
        #filtramos el contexto con el arreglo anterior
        context['Cantidad']= len(departamentos)
        if  self.request.user.is_superuser:
            Departamentos_graficos = []            
            depa = Categoria.objects.all()
            for a in depa:
                Departamentos_graficos.append({
                    'id' : a.pk,
                    'div': 'chartdivpie' + str(a.pk), 
                    'div1': 'chartdivbar' + str(a.pk), 
                    'chart' : 'chartpie' + str(a.pk),
                    'chart1' : 'chartbar' + str(a.pk)
                })                         
            context['Departamentos'] = Categoria.objects.all()
            productos = Producto.objects.values( 'subcategoria__categoria__pk',
                 'subcategoria__categoria__descripcion','genero'
                ).annotate(
                    Count('pk'), Year=Extract('creado','year')                
               )
            
            #productos = Producto.objects.all().values('subcategoria__categoria__descripcion'
            #       ).annotate(Count('pk'))
            productosinternos = ProductoINTERNO.objects.all().values(
                      'subcategoria__categoria__descripcion','estado'
                   ).annotate(Count('pk'))
            productossinregistro = ProductoSINREGISTRO.objects.all().values(
                      'subcategoria__categoria__descripcion','estado'
                   ).annotate(Count('pk'))
        else:
            context['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
            #Productos Externos
            productos = Producto.objects.filter(subcategoria__categoria__pk__in =departamentos).values(
                      'subcategoria__categoria__descripcion'
                   ).annotate(Count('pk'))
		    #Productos Internos
            productosinternos = ProductoINTERNO.objects.filter(subcategoria__categoria__pk__in =departamentos).values(
                      'subcategoria__categoria__descripcion'
                   ).annotate(Count('pk'))
		    #Productos Sin registro
            productossinregistro = ProductoSINREGISTRO.objects.filter(subcategoria__categoria__pk__in =departamentos).values(
                      'subcategoria__categoria__descripcion'
                   ).annotate(Count('pk'))
        p1 = []
        print(productos)
        for p in productos:
            p1.append(
            {
                'year': p['Year'], 
                'pk': p['subcategoria__categoria__pk'],
                'Departamento' : p['subcategoria__categoria__descripcion'] ,
                'Genero' : p['genero'],
                'Cantidad' : p['pk__count']             
            })
        context['dep_grap'] = Perfil.objects.filter(user = self.request.user)
        context['productos'] = p1
        context['productosinternos'] = productosinternos
        context['productossinregistro'] = productossinregistro
        context['departamentos_graficos'] = Departamentos_graficos
        return context

class HomeSinPrivilegios(generic.TemplateView):
    template_name="generales/sin_privilegios.html"


#class Home(LoginRequiredMixin, generic.TemplateView):
 #   template_name='generales/home.html'
  #  login_url='generales:login'
