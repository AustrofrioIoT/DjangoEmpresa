# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
tconta_taf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import usuarios.views as usuarios_views
import usuarios.login_tools as usuarios_login_tools
import fmaestros.views as fmaestros_views
import pcontable.views as pcontable_views


urlpatterns = [
# ('^my_page/$', csrf_exempt(direct_to_template), {'template': 'my_page.html'})
    url(r'^admin/', admin.site.urls),
    url(r'^$', usuarios_views.bienvenido, name='home'),

    # url(r'^password_change/$', usuarios_login_tools.Change_Password),
    # url(r'^forgotten_password/$', usuarios_views.forgotten_password),
    url(r'^login/$', usuarios_login_tools.my_login),
    url(r'^logout/$', usuarios_login_tools.my_logout),
    url(r'^accounts/login/$', usuarios_login_tools.my_login),
    url(r'^accounts/logout/$', usuarios_login_tools.my_logout),

    url(r'^accounts/profile/$', usuarios_views.bienvenido),
    url(r'^profile/$', usuarios_views.bienvenido),

    # url(r'^profile/$', usuarios_views.bienvenido, name='facturas'),
    # url(r'^profile/$', usuarios_views.bienvenido, name='resumen'),
    url(r'^accounts/password_change/$', usuarios_login_tools.Change_Password, name='cambiar_passwd'),
    url(r'^accounts/logout/$', usuarios_login_tools.my_logout, name='salir'),

    url(r'^usuarios/$', fmaestros_views.usuarios_listado, name='fich-usuarios-list'),
    url(r'^usuarios/list/$', fmaestros_views.usuarios_listado, name='fich-usuarios-list'),
    url(r'^usuarios/list/add/$', fmaestros_views.usuarios_nuevo, name='fich-usuarios-nuevo'),
    url(r'^usuarios/add/$', fmaestros_views.usuarios_nuevo, name='fich-usuarios-nuevo'),
    url(r'^usuarios/edit/$', fmaestros_views.usuarios_editar, name='fich-usuarios-editar'),
    url(r'^usuarios/remove/$', fmaestros_views.usuarios_borrar, name='fich-usuarios-borrar'),
    url(r'^usuarios/print/$', fmaestros_views.usuarios_imprimir, name='fich-usuarios-imprimir'),
    url(r'^usuarios/reestablece_password/$', fmaestros_views.usuarios_reestablece_password,
        name='fich-usuarios-reestablece_password'),

    url(r'^empresas/$', fmaestros_views.empresas_listado, name='fich-empresas-list'),
    url(r'^empresas/list/$', fmaestros_views.empresas_listado, name='fich-empresas-list'),
    url(r'^empresas/list/add/$', fmaestros_views.empresas_nuevo, name='fich-empresas-nuevo'),
    url(r'^empresas/add/$', fmaestros_views.empresas_nuevo, name='fich-empresas-nuevo'),
    url(r'^empresas/edit/$', fmaestros_views.empresas_editar, name='fich-empresas-editar'),
    url(r'^empresas/remove/$', fmaestros_views.empresas_borrar, name='fich-empresas-borrar'),
    url(r'^empresas/print/$', fmaestros_views.empresas_imprimir, name='fich-empresas-imprimir'),

    url(r'^cuentas/$',          fmaestros_views.cuentas_listado,  name='fich-cuentas-list'),
    url(r'^cuentas/list/$',     fmaestros_views.cuentas_listado,  name='fich-cuentas-list'),
    url(r'^cuentas/list/add/$', fmaestros_views.cuentas_nuevo,    name='fich-cuentas-nuevo'),
    url(r'^cuentas/add/$',      fmaestros_views.cuentas_nuevo,    name='fich-cuentas-nuevo'),
    url(r'^cuentas/edit/$',     fmaestros_views.cuentas_editar,   name='fich-cuentas-editar'),
    url(r'^cuentas/remove/$',   fmaestros_views.cuentas_borrar,   name='fich-cuentas-borrar'),
    url(r'^cuentas/print/$',    fmaestros_views.cuentas_imprimir, name='fich-cuentas-imprimir'),

    url(r'^apuntes/$',          fmaestros_views.apuntes_listado,  name='fich-apuntes-list'),
    url(r'^apuntes/list/$',     fmaestros_views.apuntes_listado,  name='fich-apuntes-list'),
    url(r'^apuntes/list/add/$', fmaestros_views.apuntes_nuevo,    name='fich-apuntes-nuevo'),
    url(r'^apuntes/add/$',      fmaestros_views.apuntes_nuevo,    name='fich-apuntes-nuevo'),
    url(r'^apuntes/edit/$',     fmaestros_views.apuntes_editar,   name='fich-apuntes-editar'),
    url(r'^apuntes/remove/$',   fmaestros_views.apuntes_borrar,   name='fich-apuntes-borrar'),
    url(r'^apuntes/print/$',    fmaestros_views.apuntes_imprimir, name='fich-apuntes-imprimir'),

    url(r'^pcontable/gastos_e_ingresos/$',    pcontable_views.relacion_gastos_ingresos, name='relacion_gastos_ingresos'),




# _____________ INI Código añadido por crea_prototipo_fmaestros.py
 
    url(r'^obras/$',          fmaestros_views.obras_listado,  name='obras-list'),
    url(r'^obras/list/$',     fmaestros_views.obras_listado,  name='obras-list'),
    url(r'^obras/list/add/$', fmaestros_views.obras_nuevo,    name='obras-nuevo'),
    url(r'^obras/add/$',      fmaestros_views.obras_nuevo,    name='obras-nuevo'),
    url(r'^obras/edit/$',     fmaestros_views.obras_editar,   name='obras-editar'),
    url(r'^obras/remove/$',   fmaestros_views.obras_borrar,   name='obras-borrar'),
    url(r'^obras/print/$',    fmaestros_views.obras_imprimir, name='obras-imprimir'),
    
# _______________ FIN Código añadido por crea_prototipo_fmaestros.py

 

# _____________ INI Código añadido por crea_prototipo_fmaestros.py
 
    url(r'^obras/$',          fmaestros_views.obras_listado,  name='obras-list'),
    url(r'^obras/list/$',     fmaestros_views.obras_listado,  name='obras-list'),
    url(r'^obras/list/add/$', fmaestros_views.obras_nuevo,    name='obras-nuevo'),
    url(r'^obras/add/$',      fmaestros_views.obras_nuevo,    name='obras-nuevo'),
    url(r'^obras/edit/$',     fmaestros_views.obras_editar,   name='obras-editar'),
    url(r'^obras/remove/$',   fmaestros_views.obras_borrar,   name='obras-borrar'),
    url(r'^obras/print/$',    fmaestros_views.obras_imprimir, name='obras-imprimir'),
    
# _______________ FIN Código añadido por crea_prototipo_fmaestros.py
]
