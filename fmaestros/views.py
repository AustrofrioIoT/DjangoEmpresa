# -*- coding: utf8 -*-

from django.http import HttpResponse
from django.conf import settings
from tconta_taf import fcomunes, menu
import models
import forms
from views_utils import listado_clase, nuevoeditar_clase, borrar_clase
from usuarios.models import Usuario
from usuarios.forms import UsuarioForm
from tconta_taf.base36crypt import genera_password

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from usuarios import models as usuarios_models
import tlalogger


#--------------  Usuarios --------------------------------------------------------
def usuarios_listado(request):
    return listado_clase(request,
                titulo_pagina='Listado de Usuarios',
                idp='fich-usuarios-list',
                formClass=None,
                modelClass=Usuario,
                pagina_listado='backoffice/fmaestros/fich-usuarios-list.html',
                pagina_formulario=None)


def usuarios_nuevo(request):
    return nuevoeditar_clase(request,
                 es_nuevo=True,
                 titulo_pagina='Nuevo Usuario',
                 idp='fich-usuarios-nuevo',
                 formClass=UsuarioForm,
                 modelClass=Usuario,
                 pagina_nuevo_dato='backoffice/fmaestros/usuario_nuevoeditar.html')


def usuarios_editar(request):
    return nuevoeditar_clase(request,
                 es_nuevo=False,
                 titulo_pagina='Editar Usuario',
                 idp='fich-usuarios-editar',
                 formClass=UsuarioForm,
                 modelClass=Usuario,
                 pagina_nuevo_dato='backoffice/fmaestros/usuario_nuevoeditar.html')

def usuarios_borrar(request):
    return borrar_clase(request,
                titulo_pagina='Borrar Usuario',
                titulo_clase='Titulares',
                idp='fich-usuarios-borrar',
                modelClass=Usuario,
                pagina_html='backoffice/fmaestros/fich_plantilla_borrar.html',
                path_cancelar='/usuarios/list/',
                success_url='/usuarios/list/')

def usuarios_imprimir(request):
    return None

@login_required
def usuarios_reestablece_password(request):
    logger = tlalogger.dj_mylogger(__file__)
    parametros = {'vengo_desde': request.META.get('HTTP_REFERER')}
    parametros['servidor_propio'] = settings.SERVIDOR_PROPIO
    parametros['titulo_pagina'] = 'Reestrablecer Password Usuario'
    parametros['subtitulo_pagina'] = ''
    usuario = usuarios_models.Usuario.objects.get(username=request.user.username)
    parametros['usuario'] = usuario
    parametros['html_menu_izquierdo'] = menu.devuelve_html_menu_izquierdo_por_usuario(usuario)

    user_id = request.GET.get('user_id').replace('.','')

    #------------------ SOLO ADMIN ----------------
    if not usuario.es_admin:
        return render(request, 'backoffice/no_permisos_para_proceso.html', parametros)

    usuario_a_modif = Usuario.objects.filter(id=user_id).last()
    if usuario_a_modif:
        password = genera_password(usuario_a_modif.username)
        usuario_a_modif.password = password
        usuario_a_modif.save()

        parametros['usuario'] = usuario_a_modif
        parametros['password'] = password

    else:
        parametros['msg_error'] = u'Usuario no encontrado. No es posible reestablecer el password.'


    return render(request, 'backoffice/fmaestros/usuario_cambiapassword.html', parametros)



#--------------  Empresas --------------------------------------------------------
def empresas_listado(request):
    return listado_clase(request,
                titulo_pagina='Listado Empresas',
                idp='fich-empresas-list',
                formClass=None,
                modelClass=models.Empresa,
                pagina_listado='backoffice/fmaestros/fich-empresas-list.html',
                pagina_formulario=None)

def empresas_nuevo(request):
    return nuevoeditar_clase(request,
                 es_nuevo=True,
                 titulo_pagina='Nuevo Empresa',
                 idp='fich-empresas-nuevo',
                 formClass=forms.EmpresaForm,
                 modelClass=models.Empresa,
                 pagina_nuevo_dato='backoffice/fmaestros/empresas-nuevo-editar.html')

def empresas_editar(request):
    return nuevoeditar_clase(request,
                 es_nuevo=False,
                 titulo_pagina='Editar Empresa',
                 idp='fich-empresas-editar',
                 formClass=forms.EmpresaForm,
                 modelClass=models.Empresa,
                 pagina_nuevo_dato='backoffice/fmaestros/empresas-nuevo-editar.html')

def empresas_borrar(request):
    return borrar_clase(request,
                titulo_pagina='Borrar Empresa',
                titulo_clase='Empresa',
                idp='fich-empresas-borrar',
                modelClass=models.Empresa,
                pagina_html='backoffice/fmaestros/fich_plantilla_borrar.html',
                path_cancelar='/empresas/list/',
                success_url='/empresas/list/')

def empresas_imprimir(request):
    return None


#--------------  Tipos de Cuentas --------------------------------------------------------
def cuentas_listado(request):
    return listado_clase(request,
                titulo_pagina='Listado Tipos de Cuentas',
                idp='fich-cuentas-list',
                formClass=None,
                modelClass=models.Cuenta,
                pagina_listado='backoffice/fmaestros/fich-cuentas-list.html',
                pagina_formulario=None)

def cuentas_nuevo(request):
    return nuevoeditar_clase(request,
                 es_nuevo=True,
                 titulo_pagina='Nuevo Tipo de Cuenta',
                 idp='fich-cuentas-nuevo',
                 formClass=forms.CuentaForm,
                 modelClass=models.Cuenta,
                 pagina_nuevo_dato='backoffice/fmaestros/cuentas-nuevo-editar.html')

def cuentas_editar(request):
    return nuevoeditar_clase(request,
                 es_nuevo=False,
                 titulo_pagina='Editar Tipo de Cuenta',
                 idp='fich-cuentas-editar',
                 formClass=forms.CuentaForm,
                 modelClass=models.Cuenta,
                 pagina_nuevo_dato='backoffice/fmaestros/cuentas-nuevo-editar.html')

def cuentas_borrar(request):
    return borrar_clase(request,
                titulo_pagina='Borrar Tipo de Cuenta',
                titulo_clase='Empresa',
                idp='fich-cuentas-borrar',
                modelClass=models.Cuenta,
                pagina_html='backoffice/fmaestros/fich_plantilla_borrar.html',
                path_cancelar='/cuentas/list/',
                success_url='/cuentas/list/')

def cuentas_imprimir(request):
    return None


#--------------  Apuntes contables --------------------------------------------------------
def apuntes_listado(request):
    return listado_clase(request,
                titulo_pagina='Listado de Gastos e Ingresos', #cambiar Titulo
                idp='fich-apuntes-list',
                formClass=None,
                modelClass=models.Apunte,
                pagina_listado='backoffice/fmaestros/apuntes-listado.html',
                pagina_formulario=None)

def apuntes_nuevo(request):
    return nuevoeditar_clase(request,
                 es_nuevo=True,
                 titulo_pagina='Nuevo Apunte Contable',
                 idp='fich-apuntes-nuevo',
                 formClass=forms.ApunteForm,
                 modelClass=models.Apunte,
                 pagina_nuevo_dato='backoffice/fmaestros/apuntes-nuevo-editar.html')

def apuntes_editar(request):
    return nuevoeditar_clase(request,
                 es_nuevo=False,
                 titulo_pagina='Editar Apunte Contable',
                 idp='fich-apuntes-editar',
                 formClass=forms.ApunteForm,
                 modelClass=models.Apunte,
                 pagina_nuevo_dato='backoffice/fmaestros/apuntes-nuevo-editar.html')

def apuntes_borrar(request):
    return borrar_clase(request,
                titulo_pagina='Borrar Apunte Contable',
                titulo_clase='Apunte Contable',
                idp='fich-apuntes-borrar',
                modelClass=models.Apunte,
                pagina_html='backoffice/fmaestros/apuntes-borrar.html',
                path_cancelar='/apuntes/list/',
                success_url='/apuntes/list/')

def apuntes_imprimir(request):
    return None

# _____________ INI Código añadido por crea_prototipo_fmaestros.py
 
    
def obras_listado(request):
    return listado_clase(request,
                titulo_pagina='Listado Obras',
                idp='obras-list',
                formClass=None,
                modelClass=models.Obra,
                pagina_listado='backoffice/fmaestros/obras-list.html',
                pagina_formulario=None)

def obras_nuevo(request):
    return nuevoeditar_clase(request,
                 es_nuevo=True,
                 titulo_pagina='Nuevo Obra',
                 idp='obras-nuevo',
                 formClass=forms.ObraForm,
                 modelClass=models.Obra,
                 # pagina_nuevo_dato='backoffice/fmaestros/obras-nuevo-editar.html')
                 pagina_nuevo_dato='backoffice/fmaestros/fich_plantilla_nuevoeditar.html')

def obras_editar(request):
    return nuevoeditar_clase(request,
                 es_nuevo=False,
                 titulo_pagina='Editar Obra',
                 idp='obras-editar',
                 formClass=forms.ObraForm,
                 modelClass=models.Obra,
                 # pagina_nuevo_dato='backoffice/fmaestros/obras-nuevo-editar.html')
                 pagina_nuevo_dato='backoffice/fmaestros/fich_plantilla_nuevoeditar.html')

def obras_borrar(request):
    return borrar_clase(request,
                titulo_pagina='Borrar Obra',
                titulo_clase='Obra',
                idp='obras-borrar',
                modelClass=models.Obra,
                pagina_html='backoffice/fmaestros/fich_plantilla_borrar.html',
                path_cancelar='/obras/list/',
                success_url='/obras/list/')

def obras_imprimir(request):
    return None
    
    
# _______________ FIN Código añadido por crea_prototipo_fmaestros.py
 
# _____________ INI Código añadido por crea_prototipo_fmaestros.py
 
    
def obras_listado(request):
    return listado_clase(request,
                titulo_pagina='Listado Obras',
                idp='obras-list',
                formClass=None,
                modelClass=models.Obra,
                pagina_listado='backoffice/fmaestros/obras-list.html',
                pagina_formulario=None)

def obras_nuevo(request):
    return nuevoeditar_clase(request,
                 es_nuevo=True,
                 titulo_pagina='Nuevo Obra',
                 idp='obras-nuevo',
                 formClass=forms.ObraForm,
                 modelClass=models.Obra,
                 # pagina_nuevo_dato='backoffice/fmaestros/obras-nuevo-editar.html')
                 pagina_nuevo_dato='backoffice/fmaestros/fich_plantilla_nuevoeditar.html')

def obras_editar(request):
    return nuevoeditar_clase(request,
                 es_nuevo=False,
                 titulo_pagina='Editar Obra',
                 idp='obras-editar',
                 formClass=forms.ObraForm,
                 modelClass=models.Obra,
                 # pagina_nuevo_dato='backoffice/fmaestros/obras-nuevo-editar.html')
                 pagina_nuevo_dato='backoffice/fmaestros/fich_plantilla_nuevoeditar.html')

def obras_borrar(request):
    return borrar_clase(request,
                titulo_pagina='Borrar Obra',
                titulo_clase='Obra',
                idp='obras-borrar',
                modelClass=models.Obra,
                pagina_html='backoffice/fmaestros/fich_plantilla_borrar.html',
                path_cancelar='/obras/list/',
                success_url='/obras/list/')

def obras_imprimir(request):
    return None
    
    
# _______________ FIN Código añadido por crea_prototipo_fmaestros.py
 