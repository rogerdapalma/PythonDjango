from django import forms
from django.db import models

class BuscaUsuarioForm(forms.Form):    

    TIPOS_USUARIOS = (
        (None, '-----'),
        ('ADMINISTRADOR', 'Administrador'),
        ('ENFERMEIRO', 'Enfermeiro' ),
        ('MÉDICO', 'Médico' ),
        ('TÉCNICO', 'Técnico' ),
    )
    tipo = forms.ChoiceField(label='Tipo ', choices=TIPOS_USUARIOS, required=False)
    nome = forms.CharField(label='Nome', max_length=100, required=False)
