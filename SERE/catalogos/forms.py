from django import forms

from catalogos.models import Categoria
from catalogos.models import SubCategoria
from catalogos.models import Producto,ProductoSINREGISTRO,ProductoINTERNO


class CategoriaForm(forms.ModelForm):
    class Meta:
       model=Categoria
       fields = ['codigop','descripcion','activo']
       labels = {"codigop":"Codigo Depto",'descripcion': "Descripcion del Departamento","activo:":"Estado"}
       widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class SubCategoriaForm(forms.ModelForm):
    categoria=forms.ModelChoiceField(
        queryset=Categoria.objects.filter(activo=True).
        order_by('descripcion')
    )
    class Meta:
       model=SubCategoria
       fields = ['categoria','codigom','descripcion','activo']
       labels = {
                'categoria':'Departamento',
                "codigom":"Codigo Municipio",
                'descripcion': "Descripcion del Municipio",
                "activo:":"Estado"}
       widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['categoria'].empty_label="Seleccione Departamento"

class ProductoForm(forms.ModelForm):    
    subcategoria = forms.ModelChoiceField(
        queryset = SubCategoria.objects.filter(activo=True).
        order_by('categoria__descripcion','descripcion'),
        empty_label="Seleccione Departamento"
    )

    class Meta:
        model = Producto
        fields = '__all__'

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })


class ProductoFormINTERNOS(forms.ModelForm):

    subcategoria = forms.ModelChoiceField(
        queryset = SubCategoria.objects.filter(activo=True).
        order_by('categoria__descripcion','descripcion'),
        empty_label="Seleccione Departamento"
    )

    class Meta:
        model = ProductoINTERNO
        fields = '__all__'

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })


class ProductoFormSINREGISTRO(forms.ModelForm):
    subcategoria = forms.ModelChoiceField(
        queryset = SubCategoria.objects.filter(activo=True).
        order_by('categoria__descripcion','descripcion'),
        empty_label="Seleccione Departamento"
    )

    class Meta:
        model = ProductoSINREGISTRO
        fields = '__all__'

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
