from django.shortcuts import render
from django.http import JsonResponse

#MODELOS BD
from .models import Asignatura
from .models import Nivel
from .models import Otec
from .models import Colegio
from .models import Capacitacion

# Create your views here.

def index(request):
    return render(request,'index.html')

def admin(request):
    return render(request,'admin.html')

def colegio(request):
    return render(request,'mant_colegio.html', {'colegios':Colegio.objects.all()} )

def add_colegio(request):
    try:
        nom = request.POST.get('nombre','')
        direccion = request.POST.get('direccion','')
        correo = request.POST.get('correo','')
        tel = request.POST.get('telefono','')

        col = Colegio.objects.filter(nombre=nom)

        if len(col) == 0 : 
            col = Colegio(nombre=nom, direccion=direccion, correo=correo, telefono=tel)
            col.save()
            data = { 
                'mensaje': 'El colegio fue registrado correctamente.', 
                'type' : 'success', 
                'tittle': 'Registro Colegio' 
            } 
            return JsonResponse(data) 

        else:    
            data = { 
                'mensaje': 'Error al registrar el colegio. El colegio ya existe.', 
                'type' : 'error', 
                'tittle': 'Registro Colegio' 
            } 
            return JsonResponse(data)
    except:
        data = { 
            'mensaje': 'Error al agregar el colegio.', 
            'type' : 'error', 
            'tittle': 'Registro Colegio' 
        } 
        return JsonResponse(data)

def edit_colegio(request, id):
    
    try:
        #Recepción de datos
        nom = request.POST.get('nombre','')
        direccion = request.POST.get('direccion','')
        correo = request.POST.get('correo','')
        tel = request.POST.get('telefono','')

        #Obtiene Objeto que se actualizará
        col = Colegio.objects.get(pk=id)

        #Actualiza objeto con datos recibidos
        col.nombre = nom
        col.direccion = direccion                                                                                                                                                                                                        
        col.correo = correo
        col.telefono = tel
        col.save() 

        data = { 
            'mensaje': 'Los datos fueron editados correctamente.', 
            'type' : 'success', 
            'tittle': 'Editar Colegio' 
        } 
        return JsonResponse(data)
    except:
        data = { 
            'mensaje': 'Error al editar los datos.', 
            'type' : 'success', 
            'tittle': 'Editar Colegio' 
        } 
        return JsonResponse(data)

def asig(request):
    return render(request,'mant_asignatura.html', {'asignaturas':Asignatura.objects.all()} )

def add_asig(request):

    try:
        nom = request.POST.get('nombre','')
        descrip = request.POST.get('descripcion','')

        asig = Asignatura.objects.filter(nombre=nom)

        if len(asig) == 0 : 
            asig = Asignatura(nombre=nom, descripcion=descrip)
            asig.save()
            data = { 
                'mensaje': 'La asignatura fue registrada correctamente.', 
                'type' : 'success', 
                'tittle': 'Registro Asignatura' 
            } 
            return JsonResponse(data) 

        else:    
            data = { 
                'mensaje': 'Error al registrar la asignatura. La asignatura ya existe.', 
                'type' : 'error', 
                'tittle': 'Registro Asignatura' 
            } 
            return JsonResponse(data)
    except:
        data = { 
            'mensaje': 'Error al agregar asignatura.', 
            'type' : 'error', 
            'tittle': 'Registro Asignatura' 
        } 
        return JsonResponse(data)

def edit_asig(request, id):
    
    try:
        #Recepción de datos
        nom = request.POST.get('nombre','')
        descrip = request.POST.get('descripcion','')

        #Obtiene Objeto que se actualizará
        asig = Asignatura.objects.get(pk=id)

        #Actualiza objeto con datos recibidos
        asig.nombre = nom
        asig.descripcion = descrip 
        asig.save() 

        data = { 
            'mensaje': 'Los datos fueron editados correctamente.', 
            'type' : 'success', 
            'tittle': 'Editar Asignatura' 
        } 
        return JsonResponse(data)
    except:
        data = { 
            'mensaje': 'Error al editar los datos.', 
            'type' : 'success', 
            'tittle': 'Editar Asignatura' 
        } 
        return JsonResponse(data)
    
def nivel(request):
    return render(request,'mant_nivel.html', {'niveles':Nivel.objects.all()} )

def add_nivel(request):
    try:
        nom = request.POST.get('nombre','')
        descrip = request.POST.get('descripcion','')

        nivel = Nivel.objects.filter(nombre=nom)

        if len(nivel) == 0 : 
            nivel = Nivel(nombre=nom, descripcion=descrip)
            nivel.save()
            data = { 
                'mensaje': 'El nivel fue registrado correctamente.', 
                'type' : 'success', 
                'tittle': 'Registro Nivel' 
            } 
            return JsonResponse(data) 

        else:    
            data = { 
                'mensaje': 'Error al registrar el nivel. El nivel ya existe.', 
                'type' : 'error', 
                'tittle': 'Registro Nivel' 
            } 
            return JsonResponse(data)
    except:
        data = { 
            'mensaje': 'Error al agregar el nivel.', 
            'type' : 'error', 
            'tittle': 'Registro Nivel' 
        } 
        return JsonResponse(data)
    
def edit_nivel(request, id):
    
    try:
        #Recepción de datos
        nom = request.POST.get('nombre','')
        descrip = request.POST.get('descripcion','')

        #Obtiene Objeto que se actualizará
        nivel = Nivel.objects.get(pk=id)

        #Actualiza objeto con datos recibidos
        nivel.nombre = nom
        nivel.descripcion = descrip 
        nivel.save() 

        data = { 
            'mensaje': 'Los datos fueron editados correctamente.', 
            'type' : 'success', 
            'tittle': 'Editar Nivel' 
        } 
        return JsonResponse(data)
    except:
        data = { 
            'mensaje': 'Error al editar los datos.', 
            'type' : 'success', 
            'tittle': 'Editar Nivel' 
        } 
        return JsonResponse(data)

def usuario(request):
    return render(request,'mant_usuario.html')

def otec(request):
    return render(request,'mant_otec.html', {'otecs':Otec.objects.all()} )

def add_otec(request):
    try:
        nom = request.POST.get('nombre','')
        direccion = request.POST.get('direccion','')
        correo = request.POST.get('correo','')
        tel = request.POST.get('telefono','')

        otec = Otec.objects.filter(nombre=nom)

        if len(otec) == 0 : 
            otec = Otec(nombre=nom, direccion=direccion, correo=correo, telefono=tel)
            otec.save()
            data = { 
                'mensaje': 'La Otec fue registrada correctamente.', 
                'type' : 'success', 
                'tittle': 'Registro Otec' 
            } 
            return JsonResponse(data) 

        else:    
            data = { 
                'mensaje': 'Error al registrar la Otec. La Otec ya existe.', 
                'type' : 'error', 
                'tittle': 'Registro Otec' 
            } 
            return JsonResponse(data)
    except:
        data = { 
            'mensaje': 'Error al agregar la Otec.', 
            'type' : 'error', 
            'tittle': 'Registro Otec' 
        } 
        return JsonResponse(data)

def edit_otec(request, id):
    
    try:
        #Recepción de datos
        nom = request.POST.get('nombre','')
        direccion = request.POST.get('direccion','')
        correo = request.POST.get('correo','')
        tel = request.POST.get('telefono','')

        #Obtiene Objeto que se actualizará
        otec = Otec.objects.get(pk=id)

        #Actualiza objeto con datos recibidos
        otec.nombre = nom
        otec.direccion = direccion                                                                                                                                                                                                        
        otec.correo = correo
        otec.telefono = tel
        otec.save() 

        data = { 
            'mensaje': 'Los datos fueron editados correctamente.', 
            'type' : 'success', 
            'tittle': 'Editar Colegio' 
        } 
        return JsonResponse(data)
    except:
        data = { 
            'mensaje': 'Error al editar los datos.', 
            'type' : 'success', 
            'tittle': 'Editar Colegio' 
        } 
        return JsonResponse(data)

def capac(request):
    return render(request,'mant_capac.html' , {'capacitaciones':Capacitacion.objects.all(), 'otecs':Otec.objects.all()})

def add_capac(request):
    try:
        nom = request.POST.get('nombre','')
        descrip = request.POST.get('descrip','')
        fecha = request.POST.get('fecha','')
        hora = request.POST.get('hora','')
        direc = request.POST.get('direccion','')
        
        otec_id = request.POST.get('otec','')
        otec = Otec.objects.get(pk=otec_id)

        capac = Capacitacion.objects.filter(nombre=nom)

        if len(capac) == 0 : 
            capac = Capacitacion(otec=otec, nombre=nom, descripcion=descrip, fecha=fecha, hora=hora, direccion=direc)
            capac.save()
            data = { 
                'mensaje': 'La Capacitación fue registrada correctamente.', 
                'type' : 'success', 
                'tittle': 'Registro Capacitación' 
            } 
            return JsonResponse(data) 

        else:    
            data = { 
                'mensaje': 'Error al registrar la Capacitación. La Capacitación ya existe.', 
                'type' : 'error', 
                'tittle': 'Registro Capacitación' 
            } 
            return JsonResponse(data)
    except:
        data = { 
            'mensaje': 'Error al agregar la Capacitación.', 
            'type' : 'error', 
            'tittle': 'Registro Capacitación' 
        } 
        return JsonResponse(data)

def edit_capac(request, id):
    
    try:
        #Recepción de datos
        nom = request.POST.get('nombre','')
        descrip = request.POST.get('descrip','')
        fecha = request.POST.get('fecha','')
        hora = request.POST.get('hora','')
        direc = request.POST.get('direccion','')
        
        otec_id = request.POST.get('otec','')
        otec = Otec.objects.get(pk=otec_id)
        
        #Obtiene Objeto que se actualizará
        capac = Capacitacion.objects.get(pk=id)

        #Actualiza objeto con datos recibidos
        capac.nombre = nom
        capac.descripcion = descrip                                                                                                                                                                                                        
        capac.fecha = fecha
        capac.hora = hora
        capac.direccion = direc 
        capac.otec.id = otec_id
        capac.save() 

        data = { 
            'mensaje': 'Los datos fueron editados correctamente.', 
            'type' : 'success', 
            'tittle': 'Editar Capacitación' 
        } 
        return JsonResponse(data)
    except:
        data = { 
            'mensaje': 'Error al editar los datos.', 
            'type' : 'error', 
            'tittle': 'Editar Capacitación' 
        } 
        return JsonResponse(data)