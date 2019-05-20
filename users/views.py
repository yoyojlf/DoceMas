# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from users.forms import UsuarioForm

# Create your views here.
def add_user(request):
    if request.method=='POST':
        usuario_form=UsuarioForm(request.POST)

        if usuario_form.is_valid:
            try:
                usuario_form.save()

                return render_to_response(
                    'users/index.html',
                    {
                        'mensaje':'ok'},
                        context_instance=RequestContext(request),
                    },
                )
            except:
                return render_to_response(
                    'users/index.html',locals(),
                    context_instance=RequestContext(request),
                    
                )
        else:
            usuario_form=UsuarioForm
        
        return render_to_response(
            'users/index.html',locals(),
            context_instance=RequestContext(request),
            
        )