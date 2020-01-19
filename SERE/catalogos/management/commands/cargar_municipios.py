from datetime import date, timedelta
from django.core.management.base import BaseCommand
from django.db.models.base import ObjectDoesNotExist
from django.contrib.auth.models import User

from ...models import Producto,SubCategoria,SACE, ProductoINTERNO,ProductoSINREGISTRO, SubCategoria, Categoria
import sys
import random

class Command(BaseCommand):
    #args = 'username...'
    help = 'Populate glucose table with random dummy data.'

    def handle(self, *args, **options):        
        sys.stdout.write('Intentando guardar productos.\n')
        for i in range(99):            
            p =  'prueba'
            p += str(i)
            region = SubCategoria(
                categoria= random.choice(Categoria.objects.all()),                
                codigo =  '0101',
                descripcion=p
            )
            region.save()               
            sys.stdout.write('Municipio Guardado con exito.\n')            

    @classmethod
    def get_date_list(cls, start, end):
        delta = end - start
        return [(start + timedelta(days=i)) for i in range(delta.days+1)]
