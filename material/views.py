from django.http import HttpResponse, JsonResponse
from django.http import response
from django.shortcuts import render, redirect
from users.models import Usuario
from users.forms import UsuarioForm, LoginForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView
from django.utils.decorators import method_decorator
from django.db.models import Q
from material.models import TypeDocument, Document
from material.forms import TypeDocumentForm, DocumentForm

from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.

# region TIPO DOCUMENTO

# Query que retorna los Tipos de material
class TypeDocumentQueryset(object):

    def get_types_queryset(self, request):
        types = TypeDocument.objects.all()
        return types


# Crea un nuevo tipo de material
class CreateTypeDocument(View):

    # @method_decorator(login_required())
    def get(self, request):
        form = TypeDocumentForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'material/add_type.html', context)

    # @method_decorator(login_required())
    def post(self, request):
        success_message = ''

        form = TypeDocumentForm(request.POST)
        if form.is_valid():

            typ = TypeDocument.objects.filter(titulo=form.cleaned_data['titulo'])

            if len(typ) == 0:
                new_type = form.save()
                data = {
                    'mensaje': 'El Tipo de Material fue registrado correctamente.',
                    'type': 'success',
                    'tittle': 'Registro Tipo de Material'
                }
                return JsonResponse(data)
            else:
                data = {
                    'mensaje': 'El Tipo de Material ya existe!.',
                    'type': 'error',
                    'tittle': 'Registro Tipo de Material'
                }
                return JsonResponse(data)
        else:
            data = {
                'mensaje': 'El Tipo de Material no se pudo registrar!.',
                'type': 'error',
                'tittle': 'Registro Tipo de Material'
            }
            return JsonResponse(data)

        # vista de los tipos de material


class ListTypesView(View):
    def get(self, request):
        types_list = TypeDocument.objects.all()

        context = {
            "types_list": types_list
        }
        return render(request, "material/list_types.html", context)


# vista para editar el Tipo de material
class TypeEditView(View, TypeDocumentQueryset):
    def get(self, request, pk):
        possible_types = self.get_types_queryset(request).filter(pk=pk)
        typ = possible_types[0] if len(possible_types) == 1 else None
        if typ is not None:
            # cargamos el detalle
            context = {
                'form': TypeDocumentForm(instance=typ),
                'id': typ.pk,
            }
            return render(request, 'material/edit_type.html', context)
        else:
            data = {
                'mensaje': 'No existe el Tipo de material!.',
                'type': 'error',
                'tittle': 'Tipo de Material'
            }
            return JsonResponse(data)

    def post(self, request, pk):
        possible_types = self.get_types_queryset(request).filter(pk=pk)
        typ = possible_types[0] if len(possible_types) == 1 else None
        if typ is not None:
            form = TypeDocumentForm(request.POST, instance=typ)
            if form.is_valid():

                tipo = TypeDocument.objects.filter(titulo=form.cleaned_data['titulo'])
                if len(tipo) == 0:
                    form.save()
                    data = {
                        'mensaje': 'El tipo de material se editó correctamente!.',
                        'type': 'success',
                        'tittle': 'Tipo de Material'
                    }
                    return JsonResponse(data)

                else:
                    data = {
                        'mensaje': 'El Tipo de Material ya existe!.',
                        'type': 'error',
                        'tittle': 'Tipo de Material'
                    }
                    return JsonResponse(data)

            else:
                data = {
                    'mensaje': 'No se puedo editar!.',
                    'type': 'error',
                    'tittle': 'Tipo de Material'
                }
                return JsonResponse(data)

            # endregion


# Query que retorna los materiales
class DocumentQueryset(object):
    @classmethod
    def get_documents_queryset(cls):
        documents = Document.objects.all()
        return documents


# Metodo para subir archivos
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'material/list_documents.html', context)
#region PruebaCreaDocument
class CreateDocumentView(View):

    @method_decorator(login_required())
    def get(self, request):
        form = DocumentForm()
        msg = ['default',]

        context = {
            'form': form,
            'msg': msg
        }
        return render(request, 'material/upload_doc.html', context)

    @method_decorator(login_required())
    def post(self, request):
        doc = Document()
        doc.owner = request.user
        form = DocumentForm(request.POST, request.FILES, instance=doc)
        msg = []
        if form.is_valid():
            form.save()
            msg.append("Doc creado correctamente")

        else:
            msg.append("DocForm no valido")

        context = { 'form': form,
                    'msg': msg, }
        return render(request,'material/upload_doc.html',context)


#endregion

# Crea un nuevo material
class CreateDocument(View):

    # @method_decorator(login_required())
    def get(self, request):
        form = DocumentForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'material/add_documento.html', context)

    # @method_decorator(login_required())
    def post(self, request):
        try:
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():

                new_document = form.save()

                data = {
                    'mensaje': 'El Material fue registrado correctamente.',
                    'type': 'success',
                    'tittle': 'Registro Material'
                }
                return JsonResponse(data)
            else:
                data = {
                    'mensaje': 'El Material no se pudo registrar!.',
                    'type': 'error',
                    'tittle': 'Registro Material'
                }
                return JsonResponse(data)
        except Exception as e:
            data = {
                'mensaje': 'Error, ' + str(e),
                'type': 'error',
                'tittle': 'Registro Material'
            }
            return JsonResponse(data)

        # vista de los materiales


class ListDocumentsView(View):
    def get(self, request):
        documents_list = Document.objects.all()
        context = {
            "documents_list": documents_list
        }
        return render(request, "material/list_documents.html", context)


# vista para editar el material
class DocumentEditView(View):
    def get(self, request, pk):
        possible_docs = DocumentQueryset.get_documents_queryset().filter(pk=pk)
        doc = possible_docs[0] if len(possible_docs) == 1 else None
        if doc is not None:
            # cargamos el detalle
            context = {
                'form': DocumentForm(instance=doc),
                'id': doc.pk,
            }
            return render(request, 'material/edit_documento.html', context)
        else:
            data = {
                'mensaje': 'No existe el material!.',
                'type': 'error',
                'tittle': 'Material'
            }
            return JsonResponse(data)

    def post(self, request, pk):
        possible_docs = get_documents_queryset(request).filter(pk=pk)
        doc = possible_docs[0] if len(possible_docs) == 1 else None
        if doc is not None:
            form = DocumentForm(request.POST, instance=doc)
            if form.is_valid():

                form.save()
                data = {
                    'mensaje': 'El material se editó correctamente!.',
                    'type': 'success',
                    'tittle': 'Material'
                }
                return JsonResponse(data)

            else:
                data = {
                    'mensaje': 'No se puedo editar!.',
                    'type': 'error',
                    'tittle': 'Material'
                }
                return JsonResponse(data)

#Edit material
class DocumentEditView(View):
    def get(self, request, pk):
        possible_docs = DocumentQueryset.get_documents_queryset().filter(pk=pk)
        doc = possible_docs[0] if len(possible_docs) == 1 else None
        if doc is not None:
            # cargamos el detalle
            context = {
                'form': DocumentForm(instance=doc),
                'id': doc.pk,
            }
            return render(request, 'material/edit_documento.html', context)
        else:
            data = {
                'mensaje': 'No existe el material!.',
                'type': 'error',
                'tittle': 'Material'
            }
            return JsonResponse(data)

    def post(self, request, pk):
        possible_docs = get_documents_queryset(request).filter(pk=pk)
        doc = possible_docs[0] if len(possible_docs) == 1 else None
        if doc is not None:
            form = DocumentForm(request.POST, instance=doc)
            if form.is_valid():

                form.save()
                data = {
                    'mensaje': 'El material se editó correctamente!.',
                    'type': 'success',
                    'tittle': 'Material'
                }
                return JsonResponse(data)

            else:
                data = {
                    'mensaje': 'No se puedo editar!.',
                    'type': 'error',
                    'tittle': 'Material'
                }
                return JsonResponse(data)


class EditDocView(View):
    @method_decorator(login_required())
    def get(self, request,pk):
        possible_docs = Document.objects.filter(pk=pk)
        doc = possible_docs[0] if len(possible_docs) == 1 else None
        msg = ['default', ]
        form = DocumentForm()
        if doc:
            form = DocumentForm(instance=doc)




        context = {
            'form': form,
            'msg': msg,
        }
        return render(request, 'material/upload_doc.html', context)

    @method_decorator(login_required())
    def post(self, request,pk):
        possible_docs = Document.objects.filter(pk=pk)
        doc = possible_docs[0] if len(possible_docs) == 1 else None
        msg = ['default', ]
        form = DocumentForm()
        if doc:
            """
            doc = Document()
            doc.pk = pk
            """
            form = DocumentForm(request.POST,instance=doc)
            if form.is_valid():
                form.save()
                msg.append("Doc creado correctamente")
            else:
                msg.append('DocForm no Valido!')
        else:
            msg.append("Doc no valido")

        context = { 'form': form,
                    'msg': msg, }
        return render(request,'material/upload_doc.html',context)
