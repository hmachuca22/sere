from datetime import date, timedelta
from django.core.management.base import BaseCommand
from django.db.models.base import ObjectDoesNotExist
from django.contrib.auth.models import User

from ...models import Producto,SubCategoria,SACE, ProductoINTERNO,ProductoSINREGISTRO
import sys
import random

class Command(BaseCommand):
    #args = 'username...'
    help = 'Populate glucose table with random dummy data.'

    def handle(self, *args, **options):        
        sys.stdout.write('Intentando guardar productos.\n')
        for i in range(200):
            producto = Producto(
                subcategoria= random.choice(SubCategoria.objects.all()),
                identidadext= random.choice(SACE.objects.all()),
                descripcion='Prueba',
                genero=random.randint(1,2),
                edad=random.randint(6,23),
                grado=random.randint(1,14),
                centroeducativo='CEntro prueba',
                codigoce='Codigo Prueba',
                origen='Prueba',
                telefono='000-00-00-00',
                idencargado='000-000-000',
                nombreencargado='0000-000-0000',
                observaciones='Prueba',
                estado=random.randint(1,5)
            )
            producto.save()               
            sys.stdout.write('Producto Guardado.\n')            

    @classmethod
    def get_date_list(cls, start, end):
        delta = end - start
        return [(start + timedelta(days=i)) for i in range(delta.days+1)]
