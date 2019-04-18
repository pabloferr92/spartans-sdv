from django.forms import ModelForm, PasswordInput
from descritivo.models.parceiro import Parceiro

class ParceiroForm(ModelForm):
    class Meta:
        model = Parceiro
        fields=['nome_provedor','razao_social','valor_pagina','valor_releaser', 'valor_policy', 'valor_tracking',
        'franquia', 'faturamento_minimo', 'usuario_dono']
