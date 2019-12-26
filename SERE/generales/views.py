from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from catalogos.models import Categoria,Perfil
from django.views import generic

# Create your views here.
class SinPrivilegios(PermissionRequiredMixin):
    login_url='generales:sin_privilegios'
    raise_exception=False
    redirect_field_name="redirecto_to"
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy(self.login_url))

class HomePage(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Pagina de Inicio')


class Home(generic.TemplateView):
    template_name='generales/home.html'

class Home_user(LoginRequiredMixin, generic.TemplateView):
    template_name='generales/home_user.html'
    login_url='generales:login'
    def get_context_data(self, **kwargs):
        #Declaramos el arreglo departamento
        dep_grap = []
        departamentos = []
        context = super(Home_user, self).get_context_data(**kwargs)
        #recorremos los departamentos a los cuales tiene acceso el usuario
        for p in Perfil.objects.filter(user = self.request.user):
            departamentos.append(
                    p.departamento.id
            )
            dep_grap.append(
                    p.departamento.descripcion
            )
        #filtramos el contexto con el arreglo anterior
        context['Cantidad']= len(departamentos)
        context['Departamentos'] = Categoria.objects.filter(pk__in= departamentos)
        context['dep_grap'] = dep_grap
        return context

class HomeSinPrivilegios(generic.TemplateView):
    template_name="generales/sin_privilegios.html"


#class Home(LoginRequiredMixin, generic.TemplateView):
 #   template_name='generales/home.html'
  #  login_url='generales:login'
