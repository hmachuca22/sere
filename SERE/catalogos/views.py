from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

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
        print(self.request.user)
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

class ProductoNewINTERNOS(SuccessMessageMixin,LoginRequiredMixin,SinPrivilegios,generic.CreateView):
    permission_required = "catalogos.add_producto"
    model = ProductoINTERNO
    template_name='catalogos/producto_form_internos.html'
    context_object_name = 'obj'
    form_class=ProductoFormINTERNOS
    success_url= reverse_lazy("catalogos:producto_list_internos")
    login_url = 'generales:sin_privilegios'
    success_message="Registro Agregado correctamente"

class ProductoNewSINREGISTRO(SuccessMessageMixin,LoginRequiredMixin,SinPrivilegios,generic.CreateView):
    permission_required = "catalogos.add_producto"
    model = ProductoSINREGISTRO
    template_name='catalogos/producto_form_sinregistro.html'
    context_object_name = 'obj'
    form_class=ProductoFormSINREGISTRO
    success_url= reverse_lazy("catalogos:producto_list_sinregistro")
    login_url = 'generales:sin_privilegios'
    success_message="NNA Agregado correctamente"

class ProductoEdit(SuccessMessageMixin,LoginRequiredMixin,SinPrivilegios,generic.UpdateView):
    permission_required = "catalogos.change_producto"
    model = Producto
    template_name='catalogos/producto_form.html'
    context_object_name = 'obj'
    form_class=ProductoForm
    success_url= reverse_lazy("catalogos:producto_list")
    login_url = 'generales:sin_privilegios'
    success_message="NNA Modificado correctamente"

class ProductoEditINTERNOS(SuccessMessageMixin,LoginRequiredMixin,SinPrivilegios,generic.UpdateView):
    permission_required = "catalogos.change_producto"
    model = ProductoINTERNO
    template_name='catalogos/producto_form_internos.html'
    context_object_name = 'obj'
    form_class=ProductoFormINTERNOS
    success_url= reverse_lazy("catalogos:producto_list_internos")
    login_url = 'generales:sin_privilegios'
    success_message="Modificado correctamente"


class ProductoEditSINREGISTRO(SuccessMessageMixin,LoginRequiredMixin,SinPrivilegios,generic.UpdateView):
    permission_required = "catalogos.change_producto"
    model = ProductoSINREGISTRO
    template_name='catalogos/producto_form_sinregistro.html'
    context_object_name = 'obj'
    form_class=ProductoFormSINREGISTRO
    success_url= reverse_lazy("catalogos:producto_list_sinregistro")
    login_url = 'generales:sin_privilegios'
    success_message="Modificado correctamente"

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
