from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name = "index"),
    path('adm',views.admin, name = "admin"),
    path('colegio',views.colegio, name = "colegio"),
    path('colegio/add',views.add_colegio, name = "add_colegio"),
    path('colegio/edit/<int:id>',views.edit_colegio, name = "edit_colegio"),
    path('asig',views.asig, name = "asig"),
    path('asig/add',views.add_asig, name = "add_asig"),
    path('asig/edit/<int:id>', views.edit_asig, name = "edit_asig"),
    path('nivel',views.nivel, name = "nivel"),
    path('nivel/add',views.add_nivel, name = "add_nivel"),
    path('nivel/edit/<int:id>', views.edit_nivel, name = "edit_nivel"),
    path('usuario',views.usuario, name = "usuario"),
    path('otec',views.otec, name = "otec"),
    path('otec/add',views.add_otec, name = "add_otec"),
    path('otec/edit/<int:id>', views.edit_otec, name = "edit_otec"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)