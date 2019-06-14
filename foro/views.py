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

        hi_with_owner = Hilo()
        hi_with_owner.owner = request.user  # asigno como propietario
        form = HiloForm(request.POST, instance=hi_with_owner)
        #form = HiloForm(request.POST)
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

#Crea una respuesta a un hilo por el momento hace referencia a foro/add_rehilo.html
class CreateReHilo(View):

    #@method_decorator(login_required())
    def get(self,request):
        """
        esto cmuestra un formulario para crear una foto
        :param request:
        :return:
        """
        form = ReHiloForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'foro/add_rehilo.html', context)

    #@method_decorator(login_required())
    def post(self,request):
        """
        esto cmuestra un formulario para crear una foto y la crea
        :param request:
        :return:
        """

        success_message = ''
        re_with_owner = ReHilo()
        re_with_owner.owner = request.user  # asigno como propietario
        form = ReHiloForm(request.POST, instance=re_with_owner)

        #form = ReHiloForm(request.POST, instance=re_owner)
        if form.is_valid():
            new_user = form.save()
            #form = PhotoForm()
            success_message = 'Hilo creado con éxito'
            form = ReHiloForm()
        else:
            success_message = 'Informacion no valida'
        context = {
            'form': form,
            'success_message': success_message
        }
        return render(request, 'foro/add_rehilo.html', context)


class HilosQueryset(object):

    def get_hilos_queryset(self,request):
        """
        if not request.user.is_authenticated:
            photos = Photo.objects.filter(visibility=PUBLIC)
        elif request.user.is_superuser:
            photos = Photo.objects.all()
        else:
            photos = Photo.objects.filter(Q(owner=request.user) | Q(visibility=PUBLIC))
        """
        hilo = Hilo.objects.all()
        return hilo

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

#vista para visualizar el detalle de un usuario
class HiloDetailView(View, HilosQueryset):
    def get(self,request,pk):
        """
        Carga la página de detalle de una foto
        :param request:
        :param pk:
        :return: HttpResponse
        """
#        possible_photos = Photo.objects.filter(pk=pk).select_related('owner')
        possible_hilos = self.get_hilos_queryset(request).filter(pk=pk)#.select_related('owner')
        hilo = possible_hilos[0] if len(possible_hilos) == 1 else None
        form = ReHiloForm()
        if hilo is not None:
            rehilo = ReHilo.objects.filter(at_hilo=hilo)
            #cargamos el detalle
            context = {
                'hilo': hilo,
                'rehilo': rehilo,
                'form':form
            }
            return render(request, 'foro/hilo.html',context)
        else:
            return response.HttpResponseNotFound('No existe el hilo')#error 404

    #@method_decorator(login_required())
    def post(self,request,pk):
        """
        esto cmuestra un formulario para crear una foto y la crea
        :param request:
        :return:
        """

        success_message = ''

        possible_hilos = self.get_hilos_queryset(request).filter(pk=pk)#.select_related('owner')
        hilo = possible_hilos[0] if len(possible_hilos) == 1 else None
        re_con_hilo = ReHilo()
        re_con_hilo.at_hilo = hilo #asigno hilo al que pertenece
        re_con_hilo.titulo = "Re: "+ str(hilo.titulo)
        re_con_hilo.owner = request.user
        form = ReHiloForm(request.POST, instance=re_con_hilo)

        if form.is_valid():
            new_user = form.save()
            #form = PhotoForm()
            success_message = 'Hilo creado con éxito'


            form = ReHiloForm()
        else:
            success_message = 'Informacion no valida'
        if hilo is not None:
            rehilo = ReHilo.objects.filter(at_hilo=hilo)
            #cargamos el detalle
            context = {
                'hilo': hilo,
                'rehilo': rehilo,
                'form':form
            }
            return render(request, 'foro/hilo.html',context)
        else:
            return response.HttpResponseNotFound('No existe el hilo')#error 404




