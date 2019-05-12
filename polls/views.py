from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def admin(request):
    return render(request,'admin.html')

def colegio(request):
    return render(request,'mant_colegio.html')

def asig(request):
    return render(request,'mant_asignatura.html')
    
def nivel(request):
    return render(request,'mant_nivel.html')

def usuario(request):
    return render(request,'mant_usuario.html')