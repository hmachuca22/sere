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
            context['Departamentos'] = Categoria.objects.all()
            productos = Producto.objects.values( 'subcategoria__categoria__pk',
                 'subcategoria__categoria__descripcion','genero'
                ).annotate(
                    Count('pk'), Year=Extract('creado','year')                
               )                        
            productosinternos = ProductoINTERNO.objects.all().values(
                      'subcategoria__categoria__descripcion','estado'
                   ).annotate(
                    Count('pk'), Year=Extract('creado','year')                
                   ) 
            productossinregistro = ProductoSINREGISTRO.objects.all().values(
                      'subcategoria__categoria__descripcion','estado'
                    ).annotate(
                    Count('pk'), Year=Extract('creado','year')                
                    ) 
        else:
            context['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
            #Productos Externos
            productos = Producto.objects.filter(subcategoria__categoria__pk__in =departamentos).values(
                      'subcategoria__categoria__descripcion'
                    ).annotate(
                    Count('pk'), Year=Extract('creado','year')                
                            ) 
		    #Productos Internos
            productosinternos = ProductoINTERNO.objects.filter(subcategoria__categoria__pk__in =departamentos).values(
                      'subcategoria__categoria__descripcion'
                    ).annotate(
                    Count('pk'), Year=Extract('creado','year')                
                    ) 
		    #Productos Sin registro
            productossinregistro = ProductoSINREGISTRO.objects.filter(subcategoria__categoria__pk__in =departamentos).values(
                      'subcategoria__categoria__descripcion'
                    ).annotate(
                    Count('pk'), Year=Extract('creado','year')                
                    ) 
        p1 = []        
        for p in productos:
            p1.append(
            {
                'year': p['Year'], 
                'pk': p['subcategoria__categoria__pk'],
                'Departamento' : p['subcategoria__categoria__descripcion'] ,
                'Genero' : p['genero'],
                'Cantidad' : p['pk__count']             
            })        
        p3 = Producto.objects.values( Year=Extract('creado','year')).distinct().order_by('-Year')
        depa = Categoria.objects.all()
        for y in p3:
            for a in depa:                
                Departamentos_graficos.append({
                    'year': y['Year'],
                    'id' : a.pk,
                    'div': 'chartdivpie' + str(a.pk) + str(y['Year']),
                    'div1': 'chartdivbar' + str(a.pk) + str(y['Year']), 
                    'chart' : 'chartpie' + str(a.pk) + str(y['Year']), 
                    'chart1' : 'chartbar' + str(a.pk) + str(y['Year'])
                    })      

        context['dep_grap'] = Perfil.objects.filter(user = self.request.user)
        context['productos'] = p1
        context['anios'] = p3
        context['productosinternos'] = productosinternos
        context['productossinregistro'] = productossinregistro
        context['departamentos_graficos'] = Departamentos_graficos
        return context

class estadisticasall(generic.TemplateView):
    template_name='generales/estadisticas.html'    
    def get_context_data(self, **kwargs):
        #Declaramos el arreglo departamento
        dep_grap = []
        departamentos = []
        context = super(estadisticasall, self).get_context_data(**kwargs)                        
        context['Cantidad']= len(departamentos)
        if  self.request.user.is_superuser:
            Departamentos_graficos = []                                    
            context['Departamentos'] = Categoria.objects.all()
            productos = Producto.objects.values( 'subcategoria__categoria__pk',
                 'subcategoria__categoria__descripcion','genero'
                ).annotate(
                    Count('pk'), Year=Extract('creado','year')                
               )                        
            productosinternos = ProductoINTERNO.objects.all().values(
                      'subcategoria__categoria__descripcion','estado'
                   ).annotate(
                    Count('pk'), Year=Extract('creado','year')                
                   ) 
            productossinregistro = ProductoSINREGISTRO.objects.all().values(
                      'subcategoria__categoria__descripcion','estado'
                    ).annotate(
                    Count('pk'), Year=Extract('creado','year')                
                    )        
        p1 = []        
        for p in productos:
            p1.append(
            {
                'year': p['Year'], 
                'pk': p['subcategoria__categoria__pk'],
                'Departamento' : p['subcategoria__categoria__descripcion'] ,
                'Genero' : p['genero'],
                'Cantidad' : p['pk__count']             
            })        
        p3 = Producto.objects.values( Year=Extract('creado','year')).distinct().order_by('-Year')
        depa = Categoria.objects.all()
        for y in p3:
            for a in depa:                
                Departamentos_graficos.append({
                    'year': y['Year'],
                    'id' : a.pk,
                    'div': 'chartdivpie' + str(a.pk) + str(y['Year']),
                    'div1': 'chartdivbar' + str(a.pk) + str(y['Year']), 
                    'chart' : 'chartpie' + str(a.pk) + str(y['Year']), 
                    'chart1' : 'chartbar' + str(a.pk) + str(y['Year'])
                    }) 
                    
        context['dep_grap'] = Perfil.objects.filter(user = self.request.user)
        context['productos'] = p1
        context['anios'] = p3
        context['productosinternos'] = productosinternos
        context['productossinregistro'] = productossinregistro
        context['departamentos_graficos'] = Departamentos_graficos
        return context

class HomeSinPrivilegios(generic.TemplateView):
    template_name="generales/sin_privilegios.html"


#class Home(LoginRequiredMixin, generic.TemplateView):
 #   template_name='generales/home.html'
  #  login_url='generales:login'
