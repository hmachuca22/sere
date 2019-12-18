from django.urls import path

from catalogos.views import CategoriaView
from catalogos.views import CategoriaNew
from catalogos.views import CategoriaEdit
from catalogos.views import CategoriaDel
from catalogos.views import ProductoViewSINREGISTRO,ProductoNewSINREGISTRO,ProductoViewINTERNOS,ProductoNewINTERNOS,ProductoEditINTERNOS
from catalogos.views import SubCategoriaView,SubCategoriaNew,SubCategoriaEdit,SubCategoriaDel,ProductoView,ProductoNew,ProductoEdit,categoria_print,historial_list

urlpatterns = [

    path('productos/ATLANTIDA', ProductoView.as_view(), name='producto_list_atlantida'),
    path('producto/new/ATLANTIDA', ProductoNew.as_view(), name='producto_new'),
    path('producto/edit/ATLANTIDA/<int:pk>', ProductoEdit.as_view(), name='producto_edit'),

    path('productos/internos/ATLANTIDA', ProductoViewINTERNOS.as_view(), name='producto_list_internos'),
    path('producto/new/internos/ATLANTIDA', ProductoNewINTERNOS.as_view(), name='producto_new_internos'),
    path('producto/edit/internos/ATLANTIDA/<int:pk>', ProductoEditINTERNOS.as_view(), name='producto_edit_internos'),

    path('productos/sinregistro/ATLANTIDA', ProductoViewSINREGISTRO.as_view(), name='producto_list_sinregistro'),
    path('producto/new/sinregistro/ATLANTIDA', ProductoNewSINREGISTRO.as_view(), name='producto_new_sinregistro'),
    path('producto/edit/sinregistro/ATLANTIDA/<int:pk>', ProductoEdit.as_view(), name='producto_edit_sinregistro'),


    path('historial', historial_list, name='historial_list'),

]