# -*- coding: utf8 -*- 
# Create your views here.

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import encoding

from usuarios import models as usuarios_models

from django.conf import settings
import tlalogger

from tconta_taf import menu
# from backoffice import adatos

@login_required
def bienvenido(request):
    """
    Página inicio. 
    Controla tanto la bienvenida una vez registrado (home),
    como si se trata del servidor propio del cliente o nuestra
    web corporativa de Internet. (settings.SERVIDOR_PROPIO)
    Tambien crea o lee ContextoUsuario, que es el que define
    en que empresa_operadora y delegacion va a trabajar, y con
    qué permisos.
    """
    logger = tlalogger.dj_mylogger(__file__)
    logger.info("El usuario %s acaba de acceder al sistema", request.user.username)
    parametros={}
    parametros['servidor_propio'] = settings.SERVIDOR_PROPIO
    usuario = usuarios_models.Usuario.objects.filter(username=request.user.username).last()
    if usuario is None:
        parametros['error_msg'] = 'Usuario "%s" no dado de alta en el sistema' % request.user.username
        return render(request, "publica/login_error.html", parametros)

    parametros['usuario'] = usuario
    parametros['html_notificaciones'] = menu.devuelve_html_notificaciones()
    parametros['html_menu_izquierdo'] = menu.devuelve_html_menu_izquierdo_por_usuario(usuario)
    # parametros['html_breadcrumb'] = menu.devuelve_mapa_web(con_pagina_inicio=True, con_iconos=True)['ppal-config-usuarios_listado']['breadcrumb-html']
    parametros['titulo_pagina'] = 'Bienvenido'
    parametros['subtitulo_pagina'] = "%s" % parametros['usuario'].nombre
    # print('Parametros iniciales: %s' % repr(parametros))
    # print request
    # print request.user
    return render(request, "backoffice/bienvenido.html", parametros)

    # if request.user.is_authenticated():
    #     return redirect('/csalones/incidencias/listar-pendientes/')
    # else:
    #     return redirect('/csalones/login')


def forgotten_password(request):
    """
    """
    parametros={}
    parametros['servidor_propio'] = settings.SERVIDOR_PROPIO
    return render(request, "publica/forgotten_password.html", parametros)

    
