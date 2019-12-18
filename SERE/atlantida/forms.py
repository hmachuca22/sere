from django import forms

from catalogos.models import Categoria
from catalogos.models import SubCategoria
from catalogos.models import Producto,ProductoSINREGISTRO,ProductoINTERNO



class ProductoFormATLANTIDA(forms.ModelForm):
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


class ProductoFormINTERNOSATLANTIDA(forms.ModelForm):
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


class ProductoFormSINREGISTROATLANTIDA(forms.ModelForm):
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
