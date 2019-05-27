from django.http import HttpResponse
from django.http import response
from django.shortcuts import render, redirect
from users.models import Usuario
from users.forms import UsuarioForm, LoginForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView
from django.utils.decorators import method_decorator
from django.db.models import Q
from foro.models import Hilo, ReHilo
from foro.forms import HiloForm, ReHiloForm



# Create your views here.
class CreateHilo(View):

    #@method_decorator(login_required())
    def get(self,request):
        """
        esto cmuestra un formulario para crear una foto
        :param request:
        :return:
        """
        form = HiloForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'foro/add_hilo.html', context)

    #@method_decorator(login_required())
    def post(self,request):
        """
        esto cmuestra un formulario para crear una foto y la crea
        :param request:
        :return:
        """

        success_message = ''

        form = HiloForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            #form = PhotoForm()
            success_message = 'Hilo creado con éxito'
            form = HiloForm()
        else:
            success_message = 'Informacion no valida'
        context = {
            'form': form,
            'success_message': success_message
        }
        return render(request, 'foro/add_hilo.html', context)

class UsersQueryset(object):

    def get_users_queryset(self,request):
        """
        if not request.user.is_authenticated:
            photos = Photo.objects.filter(visibility=PUBLIC)
        elif request.user.is_superuser:
            photos = Photo.objects.all()
        else:
            photos = Photo.objects.filter(Q(owner=request.user) | Q(visibility=PUBLIC))
        """
        users = Usuario.objects.all()
        return users

#ojo esta vista es solo en caracter de prueba luego hay que modificarla para llevarla a producción
class ListHilosView(View):
    def get(self, request):
        hilos_list = Hilo.objects.all()
        """
        html = '<ul>'
        for photo in photos:
            html += '<li>'+photo.name+'</li>'
        html += '</ul>'
        """
        context = {
            "hilos_list" : hilos_list
        }
        return render(request,"foro/list_hilos.html", context)

