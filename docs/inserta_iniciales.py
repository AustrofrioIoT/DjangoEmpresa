# -*- coding: utf-8 -*-
"""

    root@superkol:/home/desarrollo/telemap/tconta_taf# ./manage.py shell

    In [1]: from docs import inserta_iniciales

    In [2]: inserta_iniciales.inserta_usuarios()
    Usuario.save(). Valor de self.dj_user_id: None
    self.dj_user.save() OK
    Usuario.save(). Valor de self.dj_user_id: None
    self.dj_user.save() OK
    Out[2]: {'l_nok': [], 'l_ok': [('jose', 1), ('alfredo', 2)]}

"""
import os
from decimal import Decimal

from usuarios.models import Usuario
from fmaestros.models import Cuenta


l_usuarios = [
    ('jose', '1111'),
    ('eva', '2222'),
]


def inserta_usuarios():
    """
    :return:
    """
    l_ok = []
    l_nok = []
    for t in l_usuarios:
        try:
            usu = Usuario(username=t[0].strip(), password=t[1], es_admin=True)
            usu.save()
            l_ok.append((usu.username, usu.id,))
        except Exception as e:
            l_nok.append((t, e,))

    return {'l_nok': l_nok, 'l_ok': l_ok}


l_cuentas = [
#  codigo, nombre
    ('01', 'GASOIL'),
    ('02', 'MATERIAL'),
    ('03', 'ALQUILER MAQUINARIA'),
    ('04', 'DESPLAZAMIENTOS'),
    ('05', 'COMIDAS'),
    ('06', 'HOTEL'),
    ('07', 'REPARACIONES MAQUINARIA'),
    ('08', 'MAQUINARIA'),
]


# insertar True para agregar las cuentas y False para borrarlas
def inserta_cuentas(borrar_actuales):
    """
    :return:
    """
    l_ok = []
    l_nok = []

    if borrar_actuales==True:
        for t in l_cuentas:
            try:
                cta = Cuenta(codigo=t[0].strip(), nombre=t[1])
                cta.save()
                l_ok.append((cta.nombre, cta.id,))
            except Exception as e:
                l_nok.append((t, e,))
    else:
        Cuenta.objects.all().delete()
    return {'l_nok': l_nok, 'l_ok': l_ok}


