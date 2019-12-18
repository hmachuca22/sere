from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin

from .models import FacturaEnc, FacturaDet
from .forms import FacturaEncForm, FacturaDetForm, DetalleFacturaFormSet
from generales.views import SinPrivilegios

# Create your views here.


class FacturaList(LoginRequiredMixin, generic.ListView):
    login_url = 'generales:login'
    model = FacturaEnc
    template_name = "salidas/facturas_list.html"
    context_object_name = "facturas"


class FacturaNew(SinPrivilegios, generic.CreateView):
    permission_required = 'salidas.change_facturaenc'
    model = FacturaEnc
    login_url = 'generales:home'
    template_name = 'salidas/factura_form.html'
    form_class = FacturaEncForm
    success_url = reverse_lazy('salidas:facturas_list')

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_factura_formset = DetalleFacturaFormSet()
        return self.render_to_response(
            self.get_context_data(
                form=form,
                detalle_factura=detalle_factura_formset
            )
        )

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_factura = DetalleFacturaFormSet(request.POST)

        if form.is_valid() and detalle_factura.is_valid():
            return self.form_valid(form, detalle_factura)
        else:
            return self.form_invalid(form, detalle_factura)

    def form_valid(self, form, detalle_factura):
        self.object = form.save()
        detalle_factura.instance = self.object
        detalle_factura.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, detalle_factura):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                detalle_factura=detalle_factura
            )
        )


class FacturaEdit(SinPrivilegios, generic.UpdateView):
    permission_required = 'salidas.change_facturaenc'
    model = FacturaEnc
    login_url = 'generales:home'
    template_name = 'salidas/factura_form.html'
    form_class = FacturaEncForm
    success_url = reverse_lazy('salidas:factura_list')

    def get_success_url(self):
        from django.urls import reverse
        return reverse('salidas:factura_edit',
        kwargs={'pk': self.get_object().id})

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalles = FacturaDet.objects.filter(factura=self.object).order_by('pk')
        detalles_data = []
        for detalle in detalles:
            d = {
                'producto': detalle.producto,
                'cantidad': detalle.cantidad,
                'precio': detalle.precio,
                'total': detalle.total
            }
            detalles_data.append(d)
        
        detalle_factura = DetalleFacturaFormSet(initial=detalles_data)
        detalle_factura.extra += len(detalles_data)
        return self.render_to_response(
            self.get_context_data(
                form=form,
                detalle_factura=detalle_factura
            )
        )

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_factura = DetalleFacturaFormSet(request.POST)
        if form.is_valid() and detalle_factura.is_valid():
            return self.form_valid(form, detalle_factura)
        else:
            return self.form_invalid(form, detalle_factura)

    def form_valid(self, form, detalle_factura):
        self.object = form.save()
        detalle_factura.instance = self.object
        FacturaDet.objects.filter(factura=self.object).delete()
        detalle_factura.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, detalle_factura):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                detalle_factura=detalle_factura
            )
        )

class FacturaDel(SinPrivilegios, generic.DeleteView):
    permission_required = "salidas:delete_facturaenc"
    model = FacturaEnc
    template_name="salidas/factura_del.html"
    context_object_name = 'obj'
    success_url = reverse_lazy("salidas:facturas_list")