from django.urls import path
from django.conf.urls import  url
from catalogos.views import *
from catalogos.models import *
from . import views as vistas_
#
#from catalogos.views import CategoriaView
#from catalogos.views import CategoriaNew
#from catalogos.views import CategoriaEdit
#from catalogos.views import CategoriaDel
#from catalogos.views import ProductoViewSINREGISTRO,ProductoNewSINREGISTRO,ProductoViewINTERNOS,ProductoNewINTERNOS,ProductoEditINTERNOS
#from catalogos.views import SubCategoriaView,SubCategoriaNew,SubCategoriaEdit,SubCategoriaDel,ProductoView,ProductoNew,ProductoEdit,categoria_print,historial_list

urlpatterns = [
    path('categorias', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    path('categoria/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categoria/delete/<int:pk>', CategoriaDel.as_view(), name='categoria_delete'),
    path('categoria/dprint', categoria_print, name='categoria_print'),
    path('categoria/dprint/<int:pk>', categoria_print, name='categoria_print_one'),
	#Lista usuarios
    url(r'^productos/listar/(?P<pk>\d+)/$',ListarProductos.as_view(model=Producto), name='listar_productos'),
	#
    path('subcategorias', SubCategoriaView.as_view(), name='subcategoria_list'),
    path('subcategorias/new', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategoria/edit/<int:pk>', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategoria/delete/<int:pk>', SubCategoriaDel.as_view(), name='subcategoria_delete'),

    path('productos/', ProductoView.as_view(), name='producto_list'),
    path('producto/new', ProductoNew.as_view(), name='producto_new'),
    path('producto/edit/<int:pk>', ProductoEdit.as_view(), name='producto_edit'),

    path('productos/internos/', ProductoViewINTERNOS.as_view(), name='producto_list_internos'),
	#Lista usuarios
	url(r'^productos/internos/listar/(?P<pk>\d+)/$',ListarProductosInternos.as_view(model=ProductoINTERNO), name='listar_productos_internos'),
	#
    path('producto/new/internos', ProductoNewINTERNOS.as_view(), name='producto_new_internos'),
    path('producto/edit/internos/<int:pk>', ProductoEditINTERNOS.as_view(), name='producto_edit_internos'),

    path('productos/sinregistro', ProductoViewSINREGISTRO.as_view(), name='producto_list_sinregistro'),
	#Lista productos sin registro
	url(r'^productos/sinregistro/listar/(?P<pk>\d+)/$',ListarProductosSinregistro.as_view(model=ProductoSINREGISTRO), name='listar_productos_sinregistro'),
	#
    path('producto/new/sinregistro', ProductoNewSINREGISTRO.as_view(), name='producto_new_sinregistro'),
    path('producto/edit/sinregistro/<int:pk>', ProductoEditSINREGISTRO.as_view(), name='producto_edit_sinregistro'),


    path('historial', historial_list, name='historial_list'),

	# para la modificación de los estados
	url(r'catalago/modificar/estadointernos', modificar_estadosinsternos.as_view(), name='modificar_internos'),
	url(r'catalago/modificar/estado', modificar_estados.as_view(), name='modificar_estados'),
	url(r'catalago/modificar/estadosinregistro', modificar_estadosinregistro.as_view(), name='modificar_sinregistro'),

]
