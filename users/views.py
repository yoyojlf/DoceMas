# -*- coding: utf-8 -*-
"""
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from users.forms import UsuarioForm
"""

# Create your views here.
"""
def add_user(request):
    if request.method=='POST':
        usuario_form=UsuarioForm(request.POST)

        if usuario_form.is_valid:
            try:
                usuario_form.save()


                context = {
                    'mensaje': 'ok',
                    'usuario_form': usuario_form
                }
                return render(request,'users/index.html', context)

            except:
                return render(request,'users/index.html')
        else:
            usuario_form=UsuarioForm
        
        return render(request,'users/index.html')
"""
#imports
from django.http import HttpResponse
from django.http import response
from django.shortcuts import render
from users.models import Usuario
from users.forms import UsuarioForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView
from django.utils.decorators import method_decorator
from django.db.models import Q
from users.models import Usuario


# probando crear clase para agregar users
class Create(View):

    #@method_decorator(login_required())
    def get(self,request):
        """
        esto cmuestra un formulario para crear una foto
        :param request:
        :return:
        """
        form = UsuarioForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'users/new_user.html', context)

    #@method_decorator(login_required())
    def post(self,request):
        """
        esto cmuestra un formulario para crear una foto y la crea
        :param request:
        :return:
        """

        success_message = ''

        form = UsuarioForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            #form = PhotoForm()
            success_message = 'Usuario guardado con éxito'
        else:
            success_message = 'Informacion no valida'
        context = {
            'form': form,
            'success_message': success_message
        }
        return render(request, 'users/new_user.html', context)


#vista para listar los usuarios OJO es solo para caracter de prueba
class ListUsersView(View):
    def get(self, request):
        users_list = Usuario.objects.all()
        """
        html = '<ul>'
        for photo in photos:
            html += '<li>'+photo.name+'</li>'
        html += '</ul>'
        """
        context = {
            "users_list" : users_list
        }
        return render(request,"users/list_users.html", context)
