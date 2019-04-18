from django.forms import ModelForm, PasswordInput
from descritivo.models.parceiro import Parceiro
from descritivo.models.banco_dados import BancoDados


class ParceiroForm(ModelForm):
    class Meta:
        model = Parceiro
        fields=['nome_provedor','razao_social','valor_pagina','valor_releaser', 'valor_policy', 'valor_tracking',
        'franquia', 'faturamento_minimo', 'usuario_dono']

class BancoForm(ModelForm):
    class Meta:
        model = BancoDados
        fields=['nome_banco','id_parceiro','volume_paginas','qtde_releaser', 'policy', 'charge_back',
        'tracking', 'isento']