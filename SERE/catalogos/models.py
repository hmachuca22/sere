from django.db import models
from generales.models import ClaseModelo
# Create your models here.



class SACE(models.Model):
    identidadsace=models.CharField(max_length=13,primary_key=True)
    descripcion=models.CharField(max_length=100)

    def __str__(self):
        return '{} : {}'.format(self.identidadsace,self.descripcion)

    class Meta:
        verbose_name_plural="Detalles de Alumno"
        verbose_name="Detalle de Alumno"

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        unique=True
    )
    codigop=models.CharField(
        max_length=2,
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = "Categorias"

class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
    )
    codigom=models.CharField(
        max_length=4,
        unique=True
    )

    def __str__(self):
        return '{} : {}'.format(self.categoria.descripcion,self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural = "Sub Categorías"
        unique_together = ('categoria','descripcion')

class Producto(ClaseModelo):
    subcategoria=models.ForeignKey(SubCategoria,on_delete=models.CASCADE)
    identidadext=models.ForeignKey(SACE,on_delete=models.CASCADE)
    descripcion=models.CharField(max_length=100)
    genero=models.CharField(max_length=1)
    edad=models.CharField(max_length=2)
    grado=models.CharField(max_length=2)
    centroeducativo=models.CharField(max_length=100)
    codigoce=models.CharField(max_length=50)
    origen=models.CharField(max_length=200)
    telefono=models.CharField(max_length=50)
    idencargado=models.CharField(max_length=13)
    nombreencargado=models.CharField(max_length=100)
    observaciones=models.CharField(max_length=200)


    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save()

    class Meta:
        verbose_name_plural= "Productos"

class ProductoINTERNO(ClaseModelo):
    subcategoria=models.ForeignKey(SubCategoria,on_delete=models.CASCADE)
    identidadext=models.ForeignKey(SACE,on_delete=models.CASCADE)
    centroeducativo=models.CharField(max_length=100)
    codigoce=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)
    NNA=models.CharField(max_length=100)
    PMTE=models.CharField(max_length=100)
    CS=models.CharField(max_length=100)
    TOTAL=models.CharField(max_length=100)
    niveleducativo=models.CharField(max_length=100)
    grado=models.CharField(max_length=30)
    edad=models.CharField(max_length=2)
    genero=models.CharField(max_length=1)
    direccion=models.CharField(max_length=200)
    destino=models.CharField(max_length=200)
    estado=models.CharField(max_length=50)
    observaciones=models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(ProductoINTERNO, self).save()

    class Meta:
        verbose_name_plural= "ProductosInternos"

class DETALLESACE(models.Model):
    identidadsace=models.ForeignKey(SACE,on_delete=models.CASCADE)
    nombresace=models.CharField(max_length=100)
    periodo=models.CharField(max_length=4)
    departamento=models.CharField(max_length=50)
    municipio=models.CharField(max_length=50)
    aldea=models.CharField(max_length=50)
    caserio=models.CharField(max_length=50)
    codcentro=models.CharField(max_length=50)
    nombrecentro=models.CharField(max_length=50)
    grado=models.CharField(max_length=50)
    telefono=models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombresace)

    class Meta:
        verbose_name_plural="Detalles de Alumno"
        verbose_name="Detalle de Alumno"

class ProductoSINREGISTRO(ClaseModelo):
    subcategoria=models.ForeignKey(SubCategoria,on_delete=models.CASCADE)
    identidadext=models.CharField(max_length=13)
    descripcion=models.CharField(max_length=100)
    genero=models.CharField(max_length=1)
    edad=models.CharField(max_length=2)
    grado=models.CharField(max_length=2)
    centroeducativo=models.CharField(max_length=100)
    codigoce=models.CharField(max_length=50)
    origen=models.CharField(max_length=200)
    telefono=models.CharField(max_length=50)
    idencargado=models.CharField(max_length=13)
    nombreencargado=models.CharField(max_length=100)
    observaciones=models.CharField(max_length=200)


    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(ProductoSINREGISTRO, self).save()

    class Meta:
        verbose_name_plural= "ProductosSINREGISTROS"

class Perfil(models.Model):
    # user = models.OneToManyField('auth.User', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    departamento = models.ForeignKey(Categoria,related_name = 'departamento',unique=True ,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.user , self.departamento)
