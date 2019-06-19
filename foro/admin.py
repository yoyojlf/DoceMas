from django.contrib import admin
from foro.models import Hilo,ReHilo

# Register your models here.
class HiloAdmin(admin.ModelAdmin):
    #form = UsuarioFormSu
    #campos a mostrar en el modelo usuario
    list_display = ('owner', 'titulo', 'descripcion', 'fecha', 'estado', 'visibility')
    list_filter = ('owner', 'fecha', 'estado', 'visibility')
    search_fields = ('owner', 'fecha', 'descripcion', )
    ordering = ('fecha',)

    """
    fieldsets = (
        (None,{'fields':('email','password',)}),
        ('Informacion Personal',{'fields':('username','first_name','last_name')}),
        #('Permisos Django',{'fields':('admin','staff','active')}),
    )
    """

    add_fieldsets = (
        (None, {
            'classes':('wide',),

        })
    )

class ReHiloAdmin(admin.ModelAdmin):
    #form = UsuarioFormSu
    #campos a mostrar en el modelo usuario
    list_display = ('owner', 'titulo', 'descripcion', 'fecha', 'estado', 'visibility', 'at_hilo',)
    list_filter = ('owner', 'fecha', 'estado', 'visibility', 'at_hilo',)
    search_fields = ('owner', 'fecha', 'descripcion', 'at_hilo',)
    ordering = ('fecha',)

    """
    fieldsets = (
        (None,{'fields':('email','password',)}),
        ('Informacion Personal',{'fields':('username','first_name','last_name')}),
        #('Permisos Django',{'fields':('admin','staff','active')}),
    )
    """

    add_fieldsets = (
        (None, {
            'classes':('wide',),

        })
    )

admin.site.register(Hilo,HiloAdmin)
admin.site.register(ReHilo,ReHiloAdmin)
