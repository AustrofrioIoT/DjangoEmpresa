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
    ('01', 'AMBIGUS'),
    ('02', 'TAQUILLA'),
    ('03', 'FUTBOL BASE'),
    ('04', 'FEDERACION'),
    ('05', 'SUBVENCIONES'),
    ('06', 'FISIO'),
    ('07', 'CAMPO MANTENIMIENTO'),
    ('08', 'CARNETS'),
    ('09', 'PATROCINIOS'),
    ('10', 'MATERIAL DEPORTIVO'),
    ('11', 'INVITACIONES'),
    ('12', 'OTROS'),
    ('13', 'VALLAS PUBLICITARIAS'),
    ('14', 'LOTERIAS Y RIFAS'),
    ('15', 'MERCHANDISING'),
    ('16', 'SUELDOS Y SALARIOS'),
    ('17', 'ARBITRAJES'),
]


def inserta_cuentas():
    """
    :return:
    """
    l_ok = []
    l_nok = []
    for t in l_cuentas:
        try:
            cta = Cuenta(codigo=t[0].strip(), nombre=t[1])
            cta.save()
            l_ok.append((cta.nombre, cta.id,))
        except Exception as e:
            l_nok.append((t, e,))

    return {'l_nok': l_nok, 'l_ok': l_ok}


