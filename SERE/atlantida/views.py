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


class ProductoViewATLANTIDA(LoginRequiredMixin,generic.ListView):
    model = Producto
    template_name = "atlantida/producto_list_atlantida.html"
    context_object_name = "obj"
    login_url = 'generales:login'

class ProductoViewINTERNOSATLANTIDA(LoginRequiredMixin,generic.ListView):
    model = ProductoINTERNO
    template_name = "catalogos/producto_list_internos.html"
    context_object_name = "obj"
    login_url = 'generales:login'

class ProductoViewSINREGISTROATLANTIDA(LoginRequiredMixin,generic.ListView):
    model = ProductoSINREGISTRO
    template_name = "catalogos/producto_list_sinregistro.html"
    context_object_name = "obj"
    login_url = 'generales:login'

class ProductoNewATLANTIDA(SuccessMessageMixin,LoginRequiredMixin,SinPrivilegios,generic.CreateView):
    permission_required = "catalogos.add_producto"
    model = Producto
    template_name='catalogos/producto_form.html'
    context_object_name = 'obj'
    form_class=ProductoForm
    success_url= reverse_lazy("catalogos:producto_list") 
    login_url = 'generales:sin_privilegios'
    success_message="NNA Agregado correctamente"

class ProductoNewINTERNOSATLANTIDA(SuccessMessageMixin,LoginRequiredMixin,SinPrivilegios,generic.CreateView):
    permission_required = "catalogos.add_producto"
    model = ProductoINTERNO
    template_name='catalogos/producto_form_internos.html'
    context_object_name = 'obj'
    form_class=ProductoFormINTERNOS
    success_url= reverse_lazy("catalogos:producto_list_internos") 
    login_url = 'generales:sin_privilegios'
    success_message="Registro Agregado correctamente"

class ProductoNewSINREGISTROATLANTIDA(SuccessMessageMixin,LoginRequiredMixin,SinPrivilegios,generic.CreateView):
    permission_required = "catalogos.add_producto"
    model = ProductoSINREGISTRO
    template_name='catalogos/producto_form_sinregistro.html'
    context_object_name = 'obj'
    form_class=ProductoFormSINREGISTRO
    success_url= reverse_lazy("catalogos:producto_list_sinregistro") 
    login_url = 'generales:sin_privilegios'
    success_message="NNA Agregado correctamente"

class ProductoEditATLANTIDA(SuccessMessageMixin,LoginRequiredMixin,SinPrivilegios,generic.UpdateView):
    permission_required = "catalogos.change_producto"
    model = Producto
    template_name='catalogos/producto_form.html'
    context_object_name = 'obj'
    form_class=ProductoForm
    success_url= reverse_lazy("catalogos:producto_list")
    login_url = 'generales:sin_privilegios'
    success_message="NNA Modificado correctamente"

class ProductoEditINTERNOSATLANTIDA(SuccessMessageMixin,LoginRequiredMixin,SinPrivilegios,generic.UpdateView):
    permission_required = "catalogos.change_producto"
    model = ProductoINTERNO
    template_name='catalogos/producto_form_internos.html'
    context_object_name = 'obj'
    form_class=ProductoFormINTERNOS
    success_url= reverse_lazy("catalogos:producto_list_internos")
    login_url = 'generales:sin_privilegios'
    success_message="Modificado correctamente"


class ProductoEditSINREGISTROATLANTIDA(SuccessMessageMixin,LoginRequiredMixin,SinPrivilegios,generic.UpdateView):
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
    return render(request,'catalogos/historial_list.html', contexto)