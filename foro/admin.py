from django.contrib import admin
from foro.models import Hilo, ReHilo

# Register your models here.
class HiloAdmin(admin.ModelAdmin):
    # form = UsuarioFormSu
    # campos a mostrar en el modelo usuario
    list_display = ( 'owner', 'titulo', 'descripcion', 'fecha', 'estado', 'visibility', )
    list_filter = ('owner', 'titulo', 'fecha', 'estado', 'visibility' )
    search_fields = ('pk', 'titulo', 'descripcion', 'fecha' )
    ordering = ('pk',)

    """

    list_display = ('name', 'pk', 'owner_name', 'license', 'visibility')
    list_filter = ('license', 'visibility')
    search_fields = ('name', 'description')

    """

    """

    fieldsets = (
        (None,{'fields':('owner', 'typeDocument', 'asignatura', 'nivel', 'titulo', 'descripcion', 'fecha', 'archivo', 'estado', 'visibility')}),
        ('Space 2',{'fields':('owner')}),

    )


    """

    add_fieldsets = (
        (None, {
            'classes': ('wide',),

        })
    )

class ReHiloAdmin(admin.ModelAdmin):
    # form = UsuarioFormSu
    # campos a mostrar en el modelo usuario
    list_display = ( 'owner', 'titulo', 'descripcion', 'fecha', 'estado', 'visibility', 'at_hilo',)
    list_filter = ('owner', 'titulo', 'fecha', 'estado', 'visibility' )
    search_fields = ('pk', 'titulo', 'descripcion', 'fecha' )
    ordering = ('pk',)

    """

    list_display = ('name', 'pk', 'owner_name', 'license', 'visibility')
    list_filter = ('license', 'visibility')
    search_fields = ('name', 'description')

    """

    """

    fieldsets = (
        (None,{'fields':('owner', 'typeDocument', 'asignatura', 'nivel', 'titulo', 'descripcion', 'fecha', 'archivo', 'estado', 'visibility')}),
        ('Space 2',{'fields':('owner')}),

    )


    """

    add_fieldsets = (
        (None, {
            'classes': ('wide',),

        })
    )


admin.site.register(Hilo,HiloAdmin)
admin.site.register(ReHilo,ReHiloAdmin)
