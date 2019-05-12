from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name = "index"),
    path('adm',views.admin, name = "admin"),
    path('colegio',views.colegio, name = "colegio"),
    path('asig',views.asig, name = "asig"),
    path('nivel',views.nivel, name = "nivel"),
    path('usuario',views.usuario, name = "usuario"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)