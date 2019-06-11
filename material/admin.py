from django.contrib import admin
from material.models import TypeDocument, Document

# Register your models here.
class Documento(admin.ModelAdmin):
    #form = UsuarioFormSu
    #campos a mostrar en el modelo usuario
    list_display = ('owner', 'typeDocument', 'asignatura', 'nivel', 'titulo', 'descripcion', 'fecha', 'archivo', 'estado', 'visibility')
    list_filter = ('owner', 'typeDocument', 'asignatura', 'nivel', 'fecha', 'estado', 'visibility')
    search_fields = ('owner', 'typeDocument', 'asignatura', 'nivel', 'fecha', 'estado', 'visibility')
    ordering = ('fecha',)

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
            'classes':('wide',),

        })
    )


class TypeDocumento(admin.ModelAdmin):
    # form = UsuarioFormSu
    # campos a mostrar en el modelo usuario
    list_display = ( 'titulo', 'descripcion', )
    list_filter = ('titulo', 'descripcion', )
    search_fields = ('pk', 'titulo', 'descripcion', )
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


admin.site.register(Document,Documento)
admin.site.register(TypeDocument,TypeDocumento)
# Register your models here.
#admin.site.register(Photo, PhotoAdmin)


