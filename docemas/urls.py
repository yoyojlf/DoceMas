"""docemas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
<<<<<<< HEAD
from users.views import Create as CreateUser, ListUsersView, LoginView, LogoutView, Edit_user
=======
from users.views import Create as CreateUser, ListUsersView, LoginView, LogoutView, UserDetailView, UserEditView
<<<<<<< HEAD
from foro.views import CreateHilo, ListHilosView
>>>>>>> master
=======
from foro.views import CreateHilo, ListHilosView, CreateReHilo, HiloDetailView
>>>>>>> yoyo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('polls.urls')),
    url(r'^adm/new_user$', CreateUser.as_view(), name='create_user'), #url normal basada en clase
    url(r'^adm/users$', ListUsersView.as_view(), name='list_users'), #url normal basada en clase
<<<<<<< HEAD
    path(r'users/edit/<int:pk>', Edit_user.as_view(), name='edit_user'),
=======
    #ver detalle usuario
    url(r'^adm/User_Detail(?P<pk>[0-9]+)$', UserDetailView.as_view(), name='user_detail'), #url normal basada en clase
    #Actualizar usuario
    url(r'^adm/user_edit/(?P<pk>[0-9]+)$', UserEditView.as_view(), name='user_edit'), #url normal basada en clase

    #url foro
    url(r'^foro/new_hilo$', CreateHilo.as_view(), name='create_hilo'), #url normal basada en clase
    #url hilos
<<<<<<< HEAD
    url(r'^foro/hilos$', ListHilosView.as_view(), name='list_hilo'), #url normal basada en clase
>>>>>>> master
=======
    url(r'^foro/all$', ListHilosView.as_view(), name='list_hilo'), #url normal basada en clase
    #url ReHilo
    url(r'^foro/re_hilo$', CreateReHilo.as_view(), name='create_rehilo'), #url normal basada en clase
    #ver detalle usuario
    url(r'^foro/hilo/(?P<pk>[0-9]+)$', HiloDetailView.as_view(), name='hilo_detail'), #url normal basada en clase
>>>>>>> yoyo

    #Login Logout
    url(r'^login$', LoginView.as_view(), name='users_login'), #url normal basada en clase
    url(r'^logout$', LogoutView.as_view(), name='users_logout'), #url normal basada en clase
]
