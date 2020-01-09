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

from catalogos.models import Categoria
from catalogos.models import SubCategoria
from catalogos.models import Producto,DETALLESACE,ProductoSINREGISTRO,ProductoINTERNO
from catalogos.forms import SubCategoriaForm,CategoriaForm,ProductoForm,ProductoFormSINREGISTRO,ProductoFormINTERNOS
from generales.views import SinPrivilegios
from catalogos.models import *

class CategoriaView(LoginRequiredMixin,generic.ListView):
    model = Categoria
    template_name = "catalogos/categoria_list.html"
    context_object_name = "obj"
    login_url = 'generales:login'
    def get_context_data(self,**kwargs):
        #Declaramos el arreglo departamento
        departamentos = []
        #recorremos los departamentos a los cuales tiene acceso el usuario
        context = super().get_context_data(**kwargs)
        for p in Perfil.objects.filter(user = self.request.user):
            departamentos.append(
                    p.departamento.id
            )
        #filtramos el contexto con el arreglo anterior
        context['Cantidad']= len(departamentos)
        context['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
        return context


class CategoriaNew(SuccessMessageMixin,LoginRequiredMixin,SinPrivilegios,generic.CreateView):
    permission_required = "catalogos.add_categoria"
    model = Categoria
    template_name='catalogos/categoria_form.html'
    context_object_name = 'obj'
    form_class=CategoriaForm
    success_url= reverse_lazy("catalogos:categoria_list")
    login_url = 'generales:sin_privilegios'
    success_message="Categoria Creada Satisfactoriamente"


class CategoriaEdit(LoginRequiredMixin,SinPrivilegios,generic.UpdateView):
    permission_required = "catalogos.change_categoria"
    model = Categoria
    template_name='catalogos/categoria_form.html'
    context_object_name = 'obj'
    form_class=CategoriaForm
    success_url= reverse_lazy("catalogos:categoria_list")
    login_url = 'generales:sin_privilegios'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['productos'] = Producto.objects.get(subcategoria__categoria__pk=self.kwargs['pk'])
        context['Producto'] = Producto.objects.filter(subcategoria__categoria__pk=self.kwargs['pk'])
        #Declaramos el arreglo departamento
        departamentos = []
        #recorremos los departamentos a los cuales tiene acceso el usuario
        context = super().get_context_data(**kwargs)
        for p in Perfil.objects.filter(user = self.request.user):
            departamentos.append(
                    p.departamento.id
            )
        #filtramos el contexto con el arreglo anterior
        context['Cantidad']= len(departamentos)
        context['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
        return context

class CategoriaDel(LoginRequiredMixin,SinPrivilegios,generic.DeleteView):
    permission_required = "catalogos.delete_categoria"
    model = Categoria
    template_name='catalogos/catalogos_del.html'
    context_object_name = 'obj'
    success_url= reverse_lazy("catalogos:categoria_list")
    login_url = 'generales:sin_privilegios'


class SubCategoriaView(LoginRequiredMixin,generic.ListView):
    model = SubCategoria
    template_name = "catalogos/subcategoria_list.html"
    context_object_name = "obj"
    login_url = 'generales:login'
    def get_context_data(self,**kwargs):
        #Declaramos el arreglo departamento
        departamentos = []
        #recorremos los departamentos a los cuales tiene acceso el usuario
        context = super().get_context_data(**kwargs)
        for p in Perfil.objects.filter(user = self.request.user):
            departamentos.append(
                    p.departamento.id
            )
        #filtramos el contexto con el arreglo anterior
        context['Cantidad']= len(departamentos)
        context['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
        return context

class SubCategoriaNew(SuccessMessageMixin,LoginRequiredMixin,SinPrivilegios,generic.CreateView):
    permission_required = "catalogos.add_subcategoria"
    model = SubCategoria
    template_name='catalogos/subcategoria_form.html'
    context_object_name = 'obj'
    form_class=SubCategoriaForm
    success_url= reverse_lazy("catalogos:subcategoria_list")
    login_url = 'generales:sin_privilegios'
    success_message="Sub Categoria Creada Satisfactoriamente"

class SubCategoriaEdit(SuccessMessageMixin,LoginRequiredMixin,SinPrivilegios,generic.UpdateView):
    permission_required = "catalogos.change_subcategoria"
    model = SubCategoria
    template_name='catalogos/subcategoria_form.html'
    context_object_name = 'obj'
    form_class=SubCategoriaForm
    success_url= reverse_lazy("catalogos:subcategoria_list")
    login_url = 'generales:sin_privilegios'
    success_message="Sub Categoria Actualizada Satisfactoriamente"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['productos'] = Producto.objects.get(subcategoria__categoria__pk=self.kwargs['pk'])
        context['Producto'] = Producto.objects.filter(subcategoria__categoria__pk=self.kwargs['pk'])
        #Declaramos el arreglo departamento
        departamentos = []
        #recorremos los departamentos a los cuales tiene acceso el usuario
        context = super().get_context_data(**kwargs)
        for p in Perfil.objects.filter(user = self.request.user):
            departamentos.append(
                    p.departamento.id
            )
        #filtramos el contexto con el arreglo anterior
        context['Cantidad']= len(departamentos)
        context['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
        return context

class SubCategoriaDel(LoginRequiredMixin,SinPrivilegios,generic.DeleteView):
    permission_required = "catalogos.delete_subcategoria"
    model = SubCategoria
    template_name='catalogos/catalogos_del.html'
    context_object_name = 'obj'
    success_url= reverse_lazy("catalogos:subcategoria_list")
    login_url = 'generales:sin_privilegios'


class ProductoView(LoginRequiredMixin,generic.ListView):
    model = Producto
    template_name = "catalogos/producto_list.html"
    context_object_name = "obj"
    login_url = 'generales:login'
#Función para la lista de los productos del departamento de ATLANTIDA

    def get_queryset(self):
        ProductoView
        productos = []
        #recorremos los departamentos a los cuales tiene acceso el usuario
        context = super().get_context_data(**kwargs)
        for p in Perfil.objects.filter(user = self.request.user):
            departamentos.append(
                    p.departamento.id
            )
        return Producto.objects.filter(subcategoria__categoria__pk =1)

    def get_context_data(self,**kwargs):
        #Declaramos el arreglo departamento
        departamentos = []
        #recorremos los departamentos a los cuales tiene acceso el usuario
        context = super().get_context_data(**kwargs)
        for p in Perfil.objects.filter(user = self.request.user):
            departamentos.append(
                    p.departamento.id
            )
        #filtramos el contexto con el arreglo anterior
        context['Cantidad']= len(departamentos)
        context['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
        return context

class ProductoViewINTERNOS(LoginRequiredMixin,generic.ListView):
    model = ProductoINTERNO
    template_name = "catalogos/producto_list_internos.html"
    context_object_name = "obj"
    login_url = 'generales:login'
    def get_context_data(self,**kwargs):
        #Declaramos el arreglo departamento
        departamentos = []
        #recorremos los departamentos a los cuales tiene acceso el usuario
        context = super().get_context_data(**kwargs)
        for p in Perfil.objects.filter(user = self.request.user):
            departamentos.append(
                    p.departamento.id
            )
        #filtramos el contexto con el arreglo anterior
        context['Cantidad']= len(departamentos)
        context['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
        return context

    def get_queryset(self):
        ProductoINTERNO
        print(self.request.user)
        return ProductoINTERNO.objects.filter(subcategoria__categoria__pk =2)


class ProductoViewSINREGISTRO(LoginRequiredMixin,generic.ListView):
    model = ProductoSINREGISTRO
    template_name = "catalogos/producto_list_sinregistro.html"
    context_object_name = "obj"
    login_url = 'generales:login'
    def get_context_data(self,**kwargs):
        #Declaramos el arreglo departamento
        departamentos = []
        #recorremos los departamentos a los cuales tiene acceso el usuario
        context = super().get_context_data(**kwargs)
        for p in Perfil.objects.filter(user = self.request.user):
            departamentos.append(
                    p.departamento.id
            )
        #filtramos el contexto con el arreglo anterior
        context['Cantidad']= len(departamentos)
        context['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
        return context

class ProductoNew(SuccessMessageMixin,LoginRequiredMixin,SinPrivilegios,generic.CreateView):
    permission_required = "catalogos.add_producto"
    model = Producto
    template_name='catalogos/producto_form.html'
    context_object_name = 'obj'
    form_class=ProductoForm
    success_url= reverse_lazy("catalogos:producto_list")
    login_url = 'generales:sin_privilegios'
    success_message="NNA Agregado correctamente"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        #departamento = SubCategoria.objects.filter(pk = form.subcategoria)
        if form.is_valid():
            cate = request.POST['subcategoria']
            departamento = SubCategoria.objects.filter(pk = cate).order_by('-id')[:1].values('categoria__pk')
            for d in departamento:
               a = d['categoria__pk']
            form.save()
            messages.add_message(request,messages.SUCCESS,'Registro Guardado correctamente')
            success_url = reverse('catalogos:listar_productos',
                                kwargs={'pk':a})
            #success_url= reverse_lazy("catalogos:listar_productos")
            # <process form cleaned data>
            return HttpResponseRedirect(success_url)
        else:
            messages.add_message(request,messages.ERROR,'Error al guardar el registro')
            return render(request, self.template_name, {'form': form})
    
    def get_context_data(self,**kwargs):
        #Declaramos el arreglo departamento
        departamentos = []
        #recorremos los departamentos a los cuales tiene acceso el usuario
        context = super().get_context_data(**kwargs)
        for p in Perfil.objects.filter(user = self.request.user):
            departamentos.append(
                    p.departamento.id
            )
        #filtramos el contexto con el arreglo anterior
        context['Cantidad']= len(departamentos)
        context['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
        return context

class ProductoNewINTERNOS(SuccessMessageMixin,LoginRequiredMixin,SinPrivilegios,generic.CreateView):
    permission_required = "catalogos.add_producto"
    model = ProductoINTERNO
    template_name='catalogos/producto_form_internos.html'
    context_object_name = 'obj'
    form_class=ProductoFormINTERNOS
    login_url = 'generales:sin_privilegios'
    success_message="Registro Agregado correctamente"
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        #departamento = SubCategoria.objects.filter(pk = form.subcategoria)
        if form.is_valid():
            cate = request.POST['subcategoria']
            departamento = SubCategoria.objects.filter(pk = cate).order_by('-id')[:1].values('categoria__pk')
            for d in departamento:
               a = d['categoria__pk']
            form.save()
            messages.add_message(request,messages.SUCCESS,'Registro Guardado correctamente')
            success_url = reverse('catalogos:listar_productos_internos',
                                kwargs={'pk':a})
            #success_url= reverse_lazy("catalogos:listar_productos")
            # <process form cleaned data>
            return HttpResponseRedirect(success_url)
        else:
            messages.add_message(request,messages.ERROR,'Error al guardar el registro')
            return render(request, self.template_name, {'form': form})

    def get_context_data(self,**kwargs):
        #Declaramos el arreglo departamento
        departamentos = []
        #recorremos los departamentos a los cuales tiene acceso el usuario
        context = super().get_context_data(**kwargs)
        for p in Perfil.objects.filter(user = self.request.user):
            departamentos.append(
                    p.departamento.id
            )
        #filtramos el contexto con el arreglo anterior
        context['Cantidad']= len(departamentos)
        context['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
        return context     


class ProductoNewSINREGISTRO(SuccessMessageMixin,LoginRequiredMixin,SinPrivilegios,generic.CreateView):
    permission_required = "catalogos.add_producto"
    model = ProductoSINREGISTRO
    template_name='catalogos/producto_form_sinregistro.html'
    context_object_name = 'obj'
    form_class=ProductoFormSINREGISTRO
    #success_url= reverse_lazy("catalogos:producto_list_sinregistro")
    login_url = 'generales:sin_privilegios'
    success_message="NNA Agregado correctamente"
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print(form.errors)
        #departamento = SubCategoria.objects.filter(pk = form.subcategoria)
        if form.is_valid():
            cate = request.POST['subcategoria']
            departamento = SubCategoria.objects.filter(pk = cate).order_by('-id')[:1].values('categoria__pk')
            for d in departamento:
               a = d['categoria__pk']
            form.save()
            messages.add_message(request,messages.SUCCESS,'Registro Guardado correctamente')
            success_url = reverse('catalogos:listar_productos_sinregistro',
                                kwargs={'pk':a})
            #success_url= reverse_lazy("catalogos:listar_productos")
            # <process form cleaned data>
            return HttpResponseRedirect(success_url)
        else:
            messages.add_message(request,messages.ERROR,'Error al guardar el registro')
            return render(request, self.template_name, {'form': form})

class ProductoEdit(SuccessMessageMixin,LoginRequiredMixin,SinPrivilegios,generic.UpdateView):
    permission_required = "catalogos.change_producto"
    model = Producto
    template_name='catalogos/producto_form.html'
    context_object_name = 'obj'
    form_class=ProductoForm
    success_url= reverse_lazy("catalogos:producto_list")
    login_url = 'generales:sin_privilegios'
    success_message="NNA Modificado correctamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['productos'] = Producto.objects.get(subcategoria__categoria__pk=self.kwargs['pk'])
        context['Producto'] = Producto.objects.filter(subcategoria__categoria__pk=self.kwargs['pk'])
        #Declaramos el arreglo departamento
        departamentos = []
        #recorremos los departamentos a los cuales tiene acceso el usuario
        context = super().get_context_data(**kwargs)
        for p in Perfil.objects.filter(user = self.request.user):
            departamentos.append(
                    p.departamento.id
            )
        #filtramos el contexto con el arreglo anterior
        context['Cantidad']= len(departamentos)
        context['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
        return context

    def post(self, request,  pk=None, *args, **kwargs):
        #form = self.form_class(request.POST)
        Pi = Producto.objects.get(pk=pk)
        form = ProductoForm(request.POST, instance = Pi)
        #departamento = SubCategoria.objects.filter(pk = form.subcategoria)
        print(form.errors)
        if form.is_valid():
            cate = request.POST['subcategoria']
            departamento = SubCategoria.objects.filter(pk = cate).order_by('-id')[:1].values('categoria__pk')
            for d in departamento:
               a = d['categoria__pk']
            form.save()
            messages.add_message(request,messages.SUCCESS,'Registro modificado correctamente')
            success_url = reverse('catalogos:listar_productos',
                                kwargs={'pk':a})
            #success_url= reverse_lazy("catalogos:listar_productos")
            # <process form cleaned data>
            return HttpResponseRedirect(success_url)
        else:
            messages.add_message(request,messages.ERROR,'Error al guardar el registro')
            return render(request, self.template_name, {'form': form})

class ProductoEditINTERNOS(SuccessMessageMixin,LoginRequiredMixin,SinPrivilegios,generic.UpdateView):
    permission_required = "catalogos.change_producto"
    model = ProductoINTERNO
    template_name='catalogos/producto_form_internos.html'
    context_object_name = 'obj'
    form_class=ProductoFormINTERNOS
    success_url= reverse_lazy("catalogos:producto_list_internos")
    login_url = 'generales:sin_privilegios'
    success_message="Modificado correctamente"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['productos'] = Producto.objects.get(subcategoria__categoria__pk=self.kwargs['pk'])
        context['Producto'] = Producto.objects.filter(subcategoria__categoria__pk=self.kwargs['pk'])
        #Declaramos el arreglo departamento
        departamentos = []
        #recorremos los departamentos a los cuales tiene acceso el usuario
        context = super().get_context_data(**kwargs)
        for p in Perfil.objects.filter(user = self.request.user):
            departamentos.append(
                    p.departamento.id
            )
        #filtramos el contexto con el arreglo anterior
        context['Cantidad']= len(departamentos)
        context['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
        return context

    def post(self, request,  pk=None, *args, **kwargs):
        #form = self.form_class(request.POST)
        Pi = ProductoINTERNO.objects.get(pk=pk)
        form = ProductoFormINTERNOS(request.POST, instance = Pi)
        #departamento = SubCategoria.objects.filter(pk = form.subcategoria)
        if form.is_valid():
            cate = request.POST['subcategoria']
            departamento = SubCategoria.objects.filter(pk = cate).order_by('-id')[:1].values('categoria__pk')
            for d in departamento:
               a = d['categoria__pk']
            form.save()
            messages.add_message(request,messages.SUCCESS,'Registro modificado correctamente')
            success_url = reverse('catalogos:listar_productos_internos',
                                kwargs={'pk':a})
            #success_url= reverse_lazy("catalogos:listar_productos")
            # <process form cleaned data>
            return HttpResponseRedirect(success_url)
        else:
            messages.add_message(request,messages.ERROR,'Error al guardar el registro')
            return render(request, self.template_name, {'form': form})




class ProductoEditSINREGISTRO(SuccessMessageMixin,LoginRequiredMixin,SinPrivilegios,generic.UpdateView):
    permission_required = "catalogos.change_producto"
    model = ProductoSINREGISTRO
    template_name='catalogos/producto_form_sinregistro.html'
    context_object_name = 'obj'
    form_class=ProductoFormSINREGISTRO
    success_url= reverse_lazy("catalogos:producto_list_sinregistro")
    login_url = 'generales:sin_privilegios'
    success_message="Modificado correctamente"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['productos'] = Producto.objects.get(subcategoria__categoria__pk=self.kwargs['pk'])
        context['Producto'] = Producto.objects.filter(subcategoria__categoria__pk=self.kwargs['pk'])
        #Declaramos el arreglo departamento
        departamentos = []
        #recorremos los departamentos a los cuales tiene acceso el usuario
        context = super().get_context_data(**kwargs)
        for p in Perfil.objects.filter(user = self.request.user):
            departamentos.append(
                    p.departamento.id
            )
        #filtramos el contexto con el arreglo anterior
        context['Cantidad']= len(departamentos)
        context['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
        return context

    def post(self, request,  pk=None, *args, **kwargs):
        #form = self.form_class(request.POST)
        Pi = ProductoSINREGISTRO.objects.get(pk=pk)
        form = ProductoFormSINREGISTRO(request.POST, instance = Pi)
        print(form.errors)
        #departamento = SubCategoria.objects.filter(pk = form.subcategoria)
        if form.is_valid():
            cate = request.POST['subcategoria']
            departamento = SubCategoria.objects.filter(pk = cate).order_by('-id')[:1].values('categoria__pk')
            for d in departamento:
               a = d['categoria__pk']
            form.save()
            messages.add_message(request,messages.SUCCESS,'Registro modificado correctamente')
            success_url = reverse('catalogos:listar_productos_sinregistro',
                                kwargs={'pk':a})
            #success_url= reverse_lazy("catalogos:listar_productos")
            # <process form cleaned data>
            return HttpResponseRedirect(success_url)
        else:
            messages.add_message(request,messages.ERROR,'Error al guardar el registro')
            return render(request, self.template_name, {'form': form})

def categoria_print(self, pk=None):
    import io
    from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import Table

    response = HttpResponse(content_type='application/pdf')
    buff = io.BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    categorias = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Categorías", styles['Heading1'])
    categorias.append(header)
    headings = ('Id', 'Descrición', 'Activo', 'Creación')
    if not pk:
        todascategorias = [(p.id, p.descripcion, p.activo, p.creado)
                           for p in Categoria.objects.all().order_by('pk')]
    else:
        todascategorias = [(p.id, p.descripcion, p.activo, p.creado)
                           for p in Categoria.objects.filter(id=pk)]

    t = Table([headings] + todascategorias)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))

    categorias.append(t)
    doc.build(categorias)
    response.write(buff.getvalue())
    buff.close()
    return response


def historial_list(request):
    historial = DETALLESACE.objects.select_related('identidadsace')
    contexto = {'historial':historial}
    #Declaramos el arreglo departamento
    departamentos = []
    #recorremos los departamentos a los cuales tiene acceso el usuario
    for p in Perfil.objects.filter(user = request.user):
        departamentos.append(
                p.departamento.id
        )
        #filtramos el contexto con el arreglo anterior
    contexto['Cantidad']= len(departamentos)
    contexto['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
    return render(request,'catalogos/historial_list.html', contexto)


# Listar solo para los filtros de departamentos seleccionados
#Productos Externos
class ListarProductos(ListView):
    model = Producto
    template_name = "catalogos/producto_list.html"
    context_object_name = "obj"
        #print('Listar productos')
    def get_queryset(self):
        p = Producto.objects.filter(subcategoria__categoria__pk=self.kwargs['pk'])
        return Producto.objects.filter(subcategoria__categoria__pk=self.kwargs['pk']).order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['productos'] = Producto.objects.get(subcategoria__categoria__pk=self.kwargs['pk'])
        context['Producto'] = Producto.objects.filter(subcategoria__categoria__pk=self.kwargs['pk'])
        dep = Producto.objects.filter(subcategoria__categoria__pk=self.kwargs['pk']).values('subcategoria__categoria__pk').distinct()
        valores = []
        lista = Producto.objects.filter(subcategoria__categoria__pk=self.kwargs['pk']).order_by('-pk')
        for d in dep:
           context['Departamento']  = d['subcategoria__categoria__pk']
        for l in lista:
           print(l.pk)
           valores.append(l.pk)
        context['Lista'] = json.dumps(valores)
        #Declaramos el arreglo departamento
        departamentos = []
        #recorremos los departamentos a los cuales tiene acceso el usuario
        for p in Perfil.objects.filter(user = self.request.user):
            departamentos.append(
                    p.departamento.id
            )
        #filtramos el contexto con el arreglo anterior
        context['Cantidad']= len(departamentos)
        context['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
        return context
    
#Listar todos los productos
class ListarProductostodos(ListView):
    model = Producto
    template_name = "catalogos/producto_list.html"
    context_object_name = "obj"
        #print('Listar productos')
    def get_queryset(self):
        p = Producto.objects.all().order_by('-pk')
        return Producto.objects.all().order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['productos'] = Producto.objects.get(subcategoria__categoria__pk=self.kwargs['pk'])
        context['Producto'] = Producto.objects.all()
        dep = Producto.objects.all().values('subcategoria__categoria__pk').distinct()
        valores = []
        lista = Producto.objects.all().order_by('-pk')
        for d in dep:
           context['Departamento']  = d['subcategoria__categoria__pk']
        for l in lista:
           print(l.pk)
           valores.append(l.pk)
        context['Lista'] = json.dumps(valores)
        #Declaramos el arreglo departamento
        departamentos = []
        #recorremos los departamentos a los cuales tiene acceso el usuario
        for p in Perfil.objects.filter(user = self.request.user):
            departamentos.append(
                    p.departamento.id
            )
        #filtramos el contexto con el arreglo anterior
        context['Cantidad']= len(departamentos)
        context['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
        return context


#Listar todos los productos
class ListarProductostodosinternos(ListView):
    model = ProductoINTERNO
    template_name = "catalogos/producto_list.html"
    context_object_name = "obj"
        #print('Listar productos')
    def get_queryset(self):
        p = ProductoINTERNO.objects.all().order_by('-pk')
        return ProductoINTERNO.objects.all().order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        context['Producto'] = ProductoINTERNO.objects.all()
        dep = ProductoINTERNO.objects.all().values('subcategoria__categoria__pk').distinct()
        valores = []
        lista = ProductoINTERNO.objects.all().order_by('-pk')
        for d in dep:
           context['Departamento']  = d['subcategoria__categoria__pk']
        for l in lista:
           print(l.pk)
           valores.append(l.pk)
        context['Lista'] = json.dumps(valores)
        #Declaramos el arreglo departamento
        departamentos = []
        #recorremos los departamentos a los cuales tiene acceso el usuario
        for p in Perfil.objects.filter(user = self.request.user):
            departamentos.append(
                    p.departamento.id
            )
        #filtramos el contexto con el arreglo anterior
        context['Cantidad']= len(departamentos)
        context['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
        return context
#Productos Internos
class ListarProductosInternos(ListView):
    model = ProductoINTERNO
    template_name = "catalogos/producto_list_internos.html"
    context_object_name = "obj"
        #print('Listar productos')
    def get_queryset(self):
        p = ProductoINTERNO.objects.filter(subcategoria__categoria__pk=self.kwargs['pk'])
        return ProductoINTERNO.objects.filter(subcategoria__categoria__pk=self.kwargs['pk']).order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['productos'] = Producto.objects.get(subcategoria__categoria__pk=self.kwargs['pk'])
        context['Producto'] = ProductoINTERNO.objects.filter(subcategoria__categoria__pk=self.kwargs['pk'])
        dep = ProductoINTERNO.objects.filter(subcategoria__categoria__pk=self.kwargs['pk']).values('subcategoria__categoria__pk').distinct()
        valores = []
        lista = ProductoINTERNO.objects.filter(subcategoria__categoria__pk=self.kwargs['pk']).order_by('-pk')
        for d in dep:
           context['Departamento']  = d['subcategoria__categoria__pk']
        for l in lista:
           print(l.pk)
           valores.append(l.pk)
        context['Lista'] = json.dumps(valores)
        #Declaramos el arreglo departamento
        departamentos = []
        #recorremos los departamentos a los cuales tiene acceso el usuario
        for p in Perfil.objects.filter(user = self.request.user):
            departamentos.append(
                    p.departamento.id
            )
        #filtramos el contexto con el arreglo anterior
        context['Cantidad']= len(departamentos)
        context['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
        return context

#Productos sin registro
class ListarProductosSinregistro(ListView):
    model = ProductoSINREGISTRO
    template_name = "catalogos/producto_list_sinregistro.html"
    context_object_name = "obj"
        #print('Listar productos')
    def get_queryset(self):
        p = ProductoSINREGISTRO.objects.filter(subcategoria__categoria__pk=self.kwargs['pk'])
        return ProductoSINREGISTRO.objects.filter(subcategoria__categoria__pk=self.kwargs['pk']).order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['productos'] = Producto.objects.get(subcategoria__categoria__pk=self.kwargs['pk'])
        context['Producto'] = ProductoSINREGISTRO.objects.filter(subcategoria__categoria__pk=self.kwargs['pk'])
        dep = ProductoSINREGISTRO.objects.filter(subcategoria__categoria__pk=self.kwargs['pk']).values('subcategoria__categoria__pk').distinct()
        valores = []
        lista = ProductoSINREGISTRO.objects.filter(subcategoria__categoria__pk=self.kwargs['pk']).order_by('-pk')
        for d in dep:
           context['Departamento']  = d['subcategoria__categoria__pk']
        for l in lista:
           print(l.pk)
           valores.append(l.pk)
        context['Lista'] = json.dumps(valores)
        #Declaramos el arreglo departamento
        departamentos = []
        #recorremos los departamentos a los cuales tiene acceso el usuario
        for p in Perfil.objects.filter(user = self.request.user):
            departamentos.append(
                    p.departamento.id
            )
        #filtramos el contexto con el arreglo anterior
        context['Cantidad']= len(departamentos)
        context['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
        return context
#Modificar estado de productos
class modificar_estados(View):
    def post(self,request,pk=None):
        departamento = request.POST['departamento_id']
        elemento = request.POST['elemento']
        id = elemento[2:-1]
        estado = elemento[-1:]
        producto = Producto.objects.filter(pk = id)
        for p in producto:
          p.estado = estado
          p.save()
        messages.add_message(request,messages.SUCCESS,'Registro actualizado correctamente')
        success_url = reverse('catalogos:listar_productos',
                            kwargs={'pk':departamento})
        return HttpResponseRedirect(success_url)
#Modificar estados de productos internos
class modificar_estadosinsternos(View):
    def post(self,request,pk=None):
        departamento = request.POST['departamento_id']
        elemento = request.POST['elemento']
        id = elemento[2:-1]
        estado = elemento[-1:]
        producto = ProductoINTERNO.objects.filter(pk = id)
        for p in producto:
          p.estado = estado
          p.save()
        messages.add_message(request,messages.SUCCESS,'Registro actualizado correctamente')
        success_url = reverse('catalogos:listar_productos_internos',
                            kwargs={'pk':departamento})
        return HttpResponseRedirect(success_url)

#Modificar estados de productos sin registro
class modificar_estadosinregistro(View):
    def post(self,request,pk=None):
        departamento = request.POST['departamento_id']
        elemento = request.POST['elemento']
        id = elemento[2:-1]
        estado = elemento[-1:]
        producto = ProductoSINREGISTRO.objects.filter(pk = id)
        for p in producto:
          p.estado = estado
          p.save()
        messages.add_message(request,messages.SUCCESS,'Registro actualizado correctamente')
        success_url = reverse('catalogos:listar_productos_internos',
                            kwargs={'pk':departamento})
        return HttpResponseRedirect(success_url)
