from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.forms import UsuarioFormSu
from users.models import Usuario

# Register your models here.
"""
class UserAdmin(BaseUserAdmin):
    form = UsuarioFormSu
    #campos a mostrar en el modelo usuario
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    fieldsets = (
        (None,{'fields':('email','password',)}),
        ('Informacion Personal',{'fields':('username','first_name','last_name')}),
        ('Permisos Django',{'fields':('admin','staff','active')}),
    )

    add_fieldsets = (
        (None, {
            'classes':('wide',),

        })
    )
"""

class UserAdmin(admin.ModelAdmin):
    #form = UsuarioFormSu
    #campos a mostrar en el modelo usuario
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    fieldsets = (
        (None,{'fields':('email','password',)}),
        ('Informacion Personal',{'fields':('username','first_name','last_name')}),
        #('Permisos Django',{'fields':('admin','staff','active')}),
    )

    add_fieldsets = (
        (None, {
            'classes':('wide',),

        })
    )

admin.site.register(Usuario,UserAdmin)
