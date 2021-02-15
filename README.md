# DjangoEmpresa

Lista de Versiones que utiliza la aplicaciones
 
 Python v2.7.16 como lenguaje de programación principal  (pendiente de migrar a 3.9 )
 - Django v1.11.2LTS como framework de desarrollo web (pendiente de migrar a 3.2 LTS)
 - jQuery v2.2.3 como biblioteca Javascript
 - Bootstrap v3.3.7 como interfaz (UI/UX)
 - AdminLTE v2.3.8 como plantillas de diseño
 - DataTables v1.10.7 para presentar la información en Tablas,
  con clases añadidas 'moneda', 'numero', 'fecha', 'fechahora' en formato español.
 - jQuery Masked Input v1.4.1  para la entrada de fechas/horas/telefonos etc ...
 - jQuery datepicker modificado al idioma español para la seleccionar fechas

Una vez presentadas las condiciones del puesto, y descrita la tecnología a
utilizar,  paso a describirle los cambios que le solicitamos sobre la aplicación
denominada "tconta_taf".
Una vez se haya descargado el tarball con el fuente de la aplicación, lea el howto.txt,
hágala funcionar, y realice los 4 cambios de la siguiente lista:

NOTA: Cuando finalice cada modificación, añada los cambios mediante
un commit de git indicando en la descripción "Modificación 1 OK", "Modificación 2 OK", etc.
 
    1.- Lo que se llama "Apuntes Contables" tanto el en menú (menu.py) como en el título de las
páginas les vamos a llamar "Gastos e Ingresos".

    2.- Las cuentas actuales (Ambigus, Taquilla, Futbol Base, ....) las vamos a borrar y vamos a
crear unas nuevas modificando la función 'docs.inserta_iniciales.inserta_cuentas()' para que
permita borrar las que existen mediante un parámetro borrar_actuales, e inserta las nuevas:    
#  codigo, nombre
    ('01', 'GASOIL'),
    ('02', 'MATERIAL'),
    ('03', 'ALQUILER MAQUINARIA'),
    ('04', 'DESPLAZAMIENTOS'),
    ('05', 'COMIDAS'),
    ('06', 'HOTEL'),
    ('07', 'REPARACIONES MAQUINARIA'),
    ('08', 'MAQUINARIA'),

    3.- La página para añadir "Apuntes Contables": http://localhost:8000/apuntes/list/add/
hay que modificarla para que se pueda utilizar desde el móvil. Ahora mismo, al
reducir el tamaño de la página, los campos "Descripción" y "Observaciones" desaparecen.

    4.- Añadir una nueva clase "Obras" de tal manera que a cada gasto/ingreso se le pueda
asociar una obra al darlo de alta en la página de "Nuevo Gasto / Ingreso" (Antes "Apuntes Contables").
La nueva clase Obras debe contar con todas las funcionalidades para altas, bajas, modificaciones
y consultas desde la aplicación web. (De manera similar Tipos de Cuentas:
http://localhost:8000/cuentas/list/,  http://localhost:8000/cuentas/add/,
http://localhost:8000/cuentas/edit/?dato_id=1, http://localhost:8000/cuentas/remove/?dato_id=1)
Y también con su propio apartado en el menú de la izquierda.
 
 Nota: Utilize el script 'crea_prototipo_fmaestros.py' para que le cree el prototipo y
 le facilite los trabajos rutinarios. Edite el fichero y en la línea 22, modifique d_config:

d_config = {
    'nombre_clase': 'Obra',
    'nombre_inicial_url': 'obras',
    'titulo_clase_singular': 'Obra',
    'titulo_clase_plural': 'Obras',
}

Guardamos y ejecutamos desde línea de comandos:

root@superkol:~/tconta# ./crea_prototipo_fmaestros.py
Siga las instrucciones que le indica el script para modificar urls.py, menu.py y
fmaestros/uitools.py.
