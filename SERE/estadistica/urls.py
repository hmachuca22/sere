from django.urls import path
from django.conf.urls import  url
from estadistica.views import *
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
	#Lista usuarios
    url(r'^estadisticas/todas/(?P<pk>\d+)/$',Estadisticasdepartamentales.as_view(model=Producto), name='estadisticas_departamentos'),    
	#
]
