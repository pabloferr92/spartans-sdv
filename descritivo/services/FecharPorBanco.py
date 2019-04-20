from descritivo.models.banco_dados import BancoDados
from descritivo.models.parceiro import Parceiro

def FecharPorBanco(id):
    banco = BancoDados.objects.get(id=id)
    #valor_volume = banco.
