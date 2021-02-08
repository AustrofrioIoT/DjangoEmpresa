# -*- coding: utf8 -*-

from django import forms

from models import Usuario # ,EmpresaOperadora, Delegacion

# class EmpresaOperadoraForm(forms.ModelForm):
#     """
#     """
#     # codigo_interno = forms.CharField(max_length=36, required=True)
#     class Meta:
#         model = EmpresaOperadora
#         localized_fields = '__all__'
#         exclude = ()
#
#     def validate_unique(self):
#         exclude = self._get_validation_exclusions()
#         try:
#             self.instance.validate_unique(exclude=exclude)
#         except forms.ValidationError as e:
#             try:
#                 del e.error_dict['nombre']  #if field1 unique validation occurs it will be omitted and form.is_valid() method pass
#             except:
#                 pass
#             self._update_errors(e) #if there are other errors in the form those will be returned to views and is_valid() method will fail.
#
#
# class DelegacionForm(forms.ModelForm):
#     """
#     """
#     # codigo_interno = forms.CharField(max_length=36, required=True)
#     class Meta:
#         model = Delegacion
#         localized_fields = '__all__'
#         exclude = ()
#
#     def validate_unique(self):
#         exclude = self._get_validation_exclusions()
#         try:
#             self.instance.validate_unique(exclude=exclude)
#         except forms.ValidationError as e:
#             try:
#                 del e.error_dict['nombre']  #if field1 unique validation occurs it will be omitted and form.is_valid() method pass
#             except:
#                 pass
#             self._update_errors(e) #if there are other errors in the form those will be returned to views and is_valid() method will fail.
"""
    dj_user = models.OneToOneField(User)
    # Campos comunes a  django.contrib.auth.model.User
    username = models.CharField(max_length=30, unique=True)        # username
    password = models.CharField(max_length=128)                    # password
    nombre = models.CharField(max_length=30, null=True, blank=True, default=None)                       # first_name
    apellidos = models.CharField(max_length=60, null=True, blank=True, default=None)                    # last_name (0..30)
    email = models.CharField(max_length=75, null=True, blank=True, default=None)                        # email
    esta_activo = models.BooleanField(default=True)                # is_active
    ultimo_acceso_correcto = models.DateTimeField(null=True, blank=True, default=None) #last_login                              # date_joined
    # Otros campos
    nif = models.CharField(max_length=15, null=True, blank=True, default=None, unique=True)
    observaciones = models.CharField(max_length=128, null=True, blank=True, default=None)
    ultimo_acceso_incorrecto = models.DateTimeField(null=True, blank=True, default=None)
    accesos_correctos = models.PositiveSmallIntegerField(default=0)
    accesos_incorrectos = models.PositiveSmallIntegerField(default=0)
    fecha_baja = models.DateField(null=True, blank=True)
    # Relacionado con los permisos
    # Si el titular es None, el usuario es "Superusuario", es decir,
    # pertenece a la operadora y lleva un menu distinto.
    titular = models.ForeignKey(fmaestros_models.Titular, null=True, blank=True)
    # El usuario debe pertenecer al menos a un grupo
    grupo = models.ManyToManyField(Grupo)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_paso_historico = models.DateTimeField(null=True, blank=True, default=None)

"""

class UsuarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.es_nuevo = kwargs.get('es_nuevo')
        if self.es_nuevo is not None:
            del kwargs['es_nuevo']
        super(UsuarioForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Usuario
        localized_fields = '__all__'
        # fields = ('username', 'nombre', 'apellidos', 'titular', 'fecha_paso_historico', 'observaciones')
        exclude = ('accesos_correctos', 'password', 'dj_user', 'accesos_incorrectos', 'grupo', )
        # exclude = ('fecha_creacion', 'fecha_modificacion', 'fecha_paso_historico')
        widgets = {
            'observaciones': forms.Textarea(attrs={'rows':2, 'cols':50}),
            'username': forms.TextInput(attrs={'size': 16}),
            'nombre': forms.TextInput(attrs={'size': 50}),
            'apellidos': forms.TextInput(attrs={'size': 50}),
        }

    def validate_unique(self, *args, **kwargs):
        if self.es_nuevo:
            super(UsuarioForm, self).validate_unique(*args, **kwargs)
        else:
            exclude = self._get_validation_exclusions()
            try:
                self.instance.validate_unique(exclude=exclude)
            except forms.ValidationError as e:
                try:
                    del e.error_dict['username']
                except:
                    pass
                self._update_errors(e)

