from django.contrib import admin
from .models import Perfil,Producto, ProductoINTERNO, ProductoSINREGISTRO
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()
admin.site.unregister(User)

class InlinePerfil(admin.TabularInline):
    model = Perfil

class CustomAdmin(UserAdmin):
    inlines = [InlinePerfil]

admin.site.register(User,CustomAdmin)
admin.site.register(Producto)
admin.site.register(ProductoINTERNO)
admin.site.register(ProductoSINREGISTRO)
# Register your models here.
from catalogos.models import Perfil
class PerfilAdmin(admin.ModelAdmin):
    pass
admin.site.register(Perfil,PerfilAdmin)
