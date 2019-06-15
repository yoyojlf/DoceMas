from django.contrib import admin
from material.models import TypeDocument, Document

# Register your models here.
class TypeDocAdmin(admin.ModelAdmin):
    #form = UsuarioFormSu
    #campos a mostrar en el modelo usuario
    list_display = ('titulo', 'descripcion',)
    list_filter = ('titulo', 'descripcion',)
    search_fields = ('titulo', 'descripcion',)
    ordering = ('titulo',)

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


class DocAdmin(admin.ModelAdmin):
    #form = UsuarioFormSu
    #campos a mostrar en el modelo usuario
    list_display = ('owner', 'typeDocument', 'asignatura', 'nivel', 'title', 'descripcion', 'fecha', 'archivo', 'estado', 'visibility',)
    list_filter = ('owner', 'typeDocument', 'asignatura', 'nivel', 'fecha', 'estado', 'visibility',)
    search_fields = ('owner', 'typeDocument', 'asignatura', 'nivel', 'title', 'descripcion', 'fecha', 'archivo', 'estado', 'visibility',)
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

admin.site.register(TypeDocument,TypeDocAdmin)

admin.site.register(Document,DocAdmin)
