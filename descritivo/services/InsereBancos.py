import csv
import xlrd
from descritivo.models.parceiro import Parceiro
from descritivo.models.banco_dados import BancoDados

planilha = xlrd.open_workbook("inputs\datacenter.xlsx")
tabela = planilha.sheet_by_name("Base Dados")

def RetornaNomesProvedores():
    parceiros = Parceiro.objects.all()
    nomes = []
    for parceiro in parceiros:
        nomes.append(parceiro.nome_provedor)
    return nomes

def LerBancosDoArquivo():
    parceiros = RetornaNomesProvedores()
    for i in range(tabela.nrows):
        if i == 0:
            continue
        linha = tabela.row_values(i)
        if str(linha[7]) in parceiros:
            print("Parceiro encontrado inserindo banco")
            nome_banco = linha[0]
            provedor = linha[7]
            volume_paginas = linha[44]
            qtde_releaser = linha[20]
            policy = linha[21]
            tracking = linha[22]
            charge_back = linha[24]
            InsereBancos(nome_banco,provedor,volume_paginas,qtde_releaser,policy,tracking,charge_back)
            
def InsereBancos(nome_banco,provedor,volume_paginas,qtde_releaser,policy,tracking,charge_back):
    provedor_aux = Parceiro.objects.get(nome_provedor=provedor)
    BancoDados.objects.create(
        nome_banco = nome_banco,
        id_parceiro = provedor_aux,
        volume_paginas = volume_paginas,
        qtde_releaser = qtde_releaser,
        policy = policy,
        tracking = tracking,
        charge_back = charge_back,
    )
