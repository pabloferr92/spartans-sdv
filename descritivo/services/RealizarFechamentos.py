from descritivo.models.parceiro import Parceiro
from descritivo.models.banco_dados import BancoDados
from descritivo.models.fechamento_banco import FechamentoBanco
from datetime import date, datetime 

def RetornaBancosPorParceiro(id):
    bancos = BancoDados.objects.filter(id_parceiro=id)
    return bancos

def FechaBancosPorParceiro(id):
    bancos = BancoDados.objects.filter(id_parceiro=id)
    for banco in bancos:
        volume_paginas = banco.volume_paginas
        valor_paginas = banco.volume_paginas * banco.id_parceiro.valor_pagina
        qtde_releaser = banco.qtde_releaser
        valor_releaser = banco.qtde_releaser * banco.id_parceiro.valor_releaser
        if banco.policy == "Sim" or banco.policy == "sim":
            volume_policy = banco.volume_paginas
            valor_policy = banco.volume_paginas * banco.id_parceiro.valor_policy
        else:
            volume_policy = 0
            valor_policy = 0
        if banco.charge_back == "Sim" or banco.charge_back == "sim":
            volume_charge_back = banco.volume_paginas
            valor_charge_back = banco.volume_paginas * banco.id_parceiro.valor_policy
        else:
            volume_charge_back = 0
            valor_charge_back = 0
        if banco.tracking == "Sim" or banco.tracking == "sim":
            volume_tracking = banco.volume_paginas
            valor_tracking = banco.volume_paginas * banco.id_parceiro.valor_tracking
        else:
            volume_tracking = 0
            valor_tracking = 0
        if (banco.isento == "Sim") or (banco.isento == "sim"):
            valor_total =  0
        else:
            valor_total = valor_paginas + valor_releaser + valor_policy + valor_tracking
        mes_referencia = "2019-04-19"

        FechamentoBanco.objects.create(
        id_banco = banco,
        volume_paginas = volume_paginas,
        valor_paginas = valor_paginas,
        qtde_releaser = qtde_releaser,
        valor_releaser = valor_releaser,
        volume_policy = volume_policy,
        valor_policy = valor_policy,
        volume_charge_back = volume_charge_back,
        valor_charge_back = valor_charge_back,
        volume_tracking = volume_tracking,
        valor_tracking = valor_tracking,
        valor_total = valor_total,
        mes_referencia = mes_referencia,
        )
    return None
    
def RetornaValorTotalPorParceiro(id):
    Total = {
        "volume_paginas" : 0,
        "valor_paginas" : 0,
        "qtde_releaser" : 0,
        "valor_releaser" : 0,
        "volume_policy" : 0,
        "valor_policy" : 0,
        "volume_charge_back" : 0,
        "valor_charge_back" : 0,
        "volume_tracking" : 0,
        "valor_tracking" : 0,
        "valor_total" : 0,
    }
    fechamentos= FechamentoBanco.objects.filter(id_banco__id_parceiro=id)
    for f in fechamentos:
        Total["volume_paginas"] += int(f.volume_paginas)
        Total["valor_paginas"] += int(f.valor_paginas)
        Total["qtde_releaser"] += int(f.qtde_releaser)
        Total["valor_releaser"] += int(f.valor_releaser)
        Total["volume_policy"] += int(f.volume_policy)
        Total["valor_policy"] += float(f.valor_policy)
        Total["volume_charge_back"]+= int(f.volume_charge_back)
        Total["valor_charge_back"] += float(f.valor_charge_back)
        Total["volume_tracking"] += int(f.volume_tracking)
        Total["valor_tracking"] += float(f.valor_tracking)
        Total["valor_total"]+= float(f.valor_total)
    return Total

def RetornaFechamentosPorParceiro(id):
    fechamentos = FechamentoBanco.objects.filter(id_banco__id_parceiro=id)
    return fechamentos