from django.contrib import admin

# Register your models here.
from catalogos.models import Perfil
class PerfilAdmin(admin.ModelAdmin):
    pass
admin.site.register(Perfil,PerfilAdmin)
