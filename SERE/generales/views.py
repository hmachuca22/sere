from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from catalogos.models import Categoria
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
        context = super(Home_user, self).get_context_data(**kwargs)
        context['Departamentos'] = Categoria.objects.all()
        print('el contexto --->')
        print(context);
        return context

class HomeSinPrivilegios(generic.TemplateView):
    template_name="generales/sin_privilegios.html"


#class Home(LoginRequiredMixin, generic.TemplateView):
 #   template_name='generales/home.html'
  #  login_url='generales:login'
