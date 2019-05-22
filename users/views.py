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
from django.http import JsonResponse
from django.http import response
from django.shortcuts import render, redirect
from users.models import Usuario
from users.forms import UsuarioForm, LoginForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView
from django.utils.decorators import method_decorator
from django.db.models import Q
from users.models import Usuario
from django.contrib.auth import logout as django_logout, authenticate, login as django_login


#Login y logout
class LoginView(View):
    def get(self,request):
        error_messages = []
        form = LoginForm()
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request,'users/login.html', context)

    def post(self, request):
        error_messages = []
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd', '')
            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append('Nombre de usuario o contraseña incorrectos')
            else:
                if user.is_active:
                    django_login(request, user)
                    url = request.GET.get('next', 'admin')
                    return redirect(url)
                else:
                    error_messages.append('El usuario no está activo')
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request,'users/login.html', context)

class LogoutView(View):
    def get(self,request):
        if request.user.is_authenticated:
            django_logout(request)
        return redirect('index')



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
            data = { 
                'mensaje': 'El usuario fue registrado correctamente.', 
                'type' : 'success', 
                'tittle': 'Registro Usuario' 
            } 
            return JsonResponse(data) 
        else:
            data = { 
                'mensaje': 'El usuario fue registrado correctamente.', 
                'type' : 'error', 
                'tittle': 'Registro Usuario' 
            } 
            return JsonResponse(data) 


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

class Edit_user(View):
    #@method_decorator(login_required())
    def get(self,request, pk):
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
        return render(request, 'users/edit_user.html', context)

    #@method_decorator(login_required())
    def post(self,request, pk):
        """
        esto cmuestra un formulario para crear una foto y la crea
        :param request:
        :return:
        """
        
        success_message = ''
        usuario =  Usuario.objects.get(pk=pk)[0]
        if request.method == "POST":
            form = UsuarioForm(request.POST, instance=usuario)
            if form.is_valid():
                usuario = form.save(commit=False)
                    
                usuario.save()
                success_message = 'Usuario guardado con éxito'
            else:
                success_message = 'Informacion no valida'
                context = {
                    'form': form,
                    'success_message': success_message
                }
                return render(request, 'users/edit_user.html', context)
        else:
            form = UsuarioForm(instance=usuario)
            return render(request, 'users/edit_user.html', {'form': form})